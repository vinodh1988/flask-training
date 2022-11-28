from config import app

@app.get('/')
def home():
    return "Flask app is running"

@app.get("/greet/<string:name>")
def greet(name):
    return "Hi!!!"+name