from datetime import datetime

from backend import db


class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(20), nullable=False, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    todo_items = db.relationship(
        "Todo",
        back_populates="todo_list",
        cascade="all",
        order_by=lambda: [Todo.timestamp.asc(), Todo.text.asc()])

    def to_json(self, include_relationship=False):
        if include_relationship is True:
            fields_mapping = ["id", "text", "todo_items"]
        else:
            fields_mapping = ["id", "text"]
        return {
            k: getattr(
                self,
                k) if k != "todo_items" else [
                todo.to_json() for todo in getattr(
                    self,
                    k)] for k in fields_mapping}


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_list_id = db.Column(db.Integer, db.ForeignKey("todo_list.id"))
    text = db.Column(db.String(80), nullable=False, index=True)
    done = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    todo_list = db.relationship(
        "TodoList",
        back_populates="todo_items",
        order_by=lambda: [TodoList.timestamp.asc(), TodoList.text.asc()])

    def to_json(self, include_relationship=False):
        if include_relationship is True:
            fields_mapping = ("id", "text", "done", "todo_list")
        else:
            fields_mapping = ("id", "text", "done")
        return {
            k: getattr(
                self,
                k) if k != "todo_list" else getattr(
                self,
                k).to_json() for k in fields_mapping}
