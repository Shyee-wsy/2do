from backend.app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def to_json(self):
        return {k: getattr(self, k) for k in ("id", "text", "done")}
