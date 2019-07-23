import click
from backend import app, db
from backend.models import Todo, TodoList
from flask import jsonify, render_template, request


# custom command
@app.cli.command("init_db")
@click.option("--drop", is_flag=True)
def init_db(drop):
    if drop is True:
        click.confirm("This operation will delete the todo database, "
                      "do you want to continue?", abort=True)
        db.drop_all()
        click.echo("Drop database success!")

    db.create_all()
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
