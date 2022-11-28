from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

basedir=os.path.abspath(os.path.dirname(__file__))

print(basedir)
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///"+os.path.join(basedir,'mydb.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db=SQLAlchemy(app)