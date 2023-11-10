
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '82세 곽춘덕 할아버지의 혼신을담은 마지막사이드와인더 발사!'

