from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>안녕</h1>'

@app.route('/<name>')
def index2(name):
    return '<h1>{} 안녕</h1>'.format(name)