from flask import Flask, render_template #import flask與render_template的套件

#flask的啟動指令：flask --app py檔名 run --debug

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.jinja.html")