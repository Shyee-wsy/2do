import os

from flask import Flask, render_template

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))  # 项目根路径，形如：.../2do

app = Flask(
    __name__,
    static_folder=os.path.join(PROJECT_ROOT, "dist"),
    template_folder=os.path.join(PROJECT_ROOT, "frontend"))


@app.route("/")
def index():
    """
    当在浏览器访问网址时，通过 render_template 方法渲染 dist 文件夹中的 index.html，
    页面之间的跳转交给前端路由负责，后端不用再写大量的路由。
    """
    return render_template("index.html")
