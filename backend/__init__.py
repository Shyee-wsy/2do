import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))  # 项目根路径，形如：.../2do

app = Flask(
    __name__,
    static_folder=os.path.join(PROJECT_ROOT, "dist"),
    template_folder=os.path.join(PROJECT_ROOT, "frontend"))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    app.root_path,
    "todo.sqlite3")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv(
    "SQLALCHEMY_TRACK_MODIFICATIONS", False)
CSRFProtect(app)
CORS(app)

db = SQLAlchemy(app)
