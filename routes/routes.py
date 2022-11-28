from config import app

@app.get('/')
def home():
    return "Flask app is running"