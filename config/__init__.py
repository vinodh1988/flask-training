from flask import Flask,send_from_directory
import os
from flask_sqlalchemy import SQLAlchemy

basedir=os.path.abspath(os.path.dirname(__file__))

print(basedir)
app=Flask(__name__,template_folder='../templates')

@app.route("/files/<path:path>")
def get_file(path):
    return send_from_directory('../static',path)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.join(basedir,'mydb.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db=SQLAlchemy(app)