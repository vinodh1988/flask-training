from config import app
from flask import render_template
@app.get('/')
def home():
    return render_template('index.html', programmer="Joseph")

@app.get("/greet/<string:name>")
def greet(name):
    return "Hi!!"+name
    