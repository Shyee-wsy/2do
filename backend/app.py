from flask import Flask, render_template

app = Flask(
    __name__,
    static_folder="../dist/static",
    template_folder="../dist")


@app.route("/")
def index():
    """
    当在浏览器访问网址时，通过 render_template 方法渲染 dist 文件夹中的 index.html，
    页面之间的跳转交给前端路由负责，后端不用再写大量的路由。
    """
    # return render_template("index.html")
    return "<h1>Hello Flask!</h1>"
