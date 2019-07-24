import random

import click
from backend import app, db
from backend.models import Todo, TodoList
from flask import jsonify, render_template, request


# help funcs
def get_default_data():
    """
    获取默认数据
    :return: iterable
    """
    return [TodoList(text="Todo")]


def get_forge_data():
    """
    获取虚拟数据
    :return: iterable
    """
    data = []
    # 生成虚拟测试数据
    todo_list_items = [
        TodoList(text="测试清单 %s" % i)
        for i in range(1, random.randint(1, 6))
    ]

    for todo_list in todo_list_items:
        todo_items = [
            Todo(text="<%s> - 测试内容 %s" % (todo_list.text, i))
            for i in range(1, random.randint(1, 11))
        ]
        todo_list.todo_items.extend(todo_items)

        data.extend(todo_items)  # 添加清单内容测试数据
    else:
        data.extend(todo_list_items)  # 添加清单测试数据
    return data


# custom command
@app.cli.command("init_db")
@click.option("--forge", is_flag=True)
def init_db(forge):
    db.drop_all()
    db.create_all()

    default_data = get_default_data()
    db.session.add_all(default_data)
    if forge is True:
        click.confirm("This operation will generate the todo forge data, "
                      "do you want to continue?", abort=True)
        forge_data = get_forge_data()
        db.session.add_all(forge_data)
    db.session.commit()

    click.echo("Initialized database success!")


# views
@app.route("/")
def index():
    """
    当在浏览器访问网址时，通过 render_template 方法渲染 frontend 文件夹中的 index.html，
    页面之间的跳转交给前端路由负责，后端不用再写大量的路由。
    """
    return render_template("index.html")


@app.route("/get_todo", methods=["GET"])
def get_todo():
    return jsonify([todo_list.to_json(include_relationship=True)
                    for todo_list in TodoList.query.order_by(TodoList.timestamp.asc()).all()])


@app.route("/new_list", methods=["POST"])
def new_list():
    todo_list = TodoList(**request.get_json())
    db.session.add(todo_list)
    db.session.commit()
    return jsonify({"status": "success", "todo": todo_list.to_json()})


@app.route("/new_todo", methods=["POST"])
def new_todo():
    todo = Todo(**request.get_json())
    db.session.add(todo)
    db.session.commit()
    return jsonify({"status": "success",
                    "todo": todo.to_json(include_relationship=True)})


@app.route("/update_todo/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    data = request.get_json()
    for k, v in data.items():
        setattr(todo, k, v)
    db.session.commit()
    return jsonify({"status": "success", "todo": todo.to_json()})


@app.route("/delete_list/<int:todo_list_id>", methods=["DELETE"])
def delete_list(todo_list_id):
    todo_list = TodoList.query.get_or_404(todo_list_id)
    db.session.delete(todo_list)
    db.session.commit()
    return jsonify({"status": "success"})


@app.route("/delete_todo/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"status": "success"})
