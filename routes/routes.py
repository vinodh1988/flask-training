from config import app
from flask import render_template
@app.get('/home')
def home():
    return render_template('index.html', programmer="Joseph")

@app.get("/greet/<string:name>")
def greet(name):
    return render_template('greet.html',name=name)
    