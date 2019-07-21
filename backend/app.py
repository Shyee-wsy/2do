import click
from flask_cors import cross_origin

from backend import app, db
from backend.models import Todo
from flask import jsonify, render_template, request


# custom command
@app.cli.command("init_db")
def init_db():
    db.create_all()
    click.echo("Initialized database sucess!")


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
    return jsonify([todo.to_json() for todo in Todo.query.all()])


@app.route("/new_todo", methods=["POST"])
def new_todo():
    todo = Todo(**request.get_json())
    db.session.add(todo)
    db.session.commit()
    return jsonify({"status": "success", "todo": todo.to_json()})


@app.route("/check_todo/<int:todo_id>", methods=["PUT"])
def check_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    data = request.get_json()
    for k, v in data.items():
        setattr(todo, k, v)
    db.session.commit()
    return jsonify({"status": "success", "todo": todo.to_json()})


@app.route("/delete_todo/<int:todo_id>", methods=["DELETE"])
@cross_origin()
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"status": "success"})
