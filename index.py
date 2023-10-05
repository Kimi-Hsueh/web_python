from flask import Flask #import flask的套件

#flask的啟動指令：flask --app py檔名 run --debug

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/second')
def second():
    return "<p>second page</p>"