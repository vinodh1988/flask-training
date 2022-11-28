from config import app,db
from database import Person
from flask import jsonify

@app.route('/people')
def getPeople():
    listp=Person.query.all()
    result=[ x.serialize() for x in listp]
    return jsonify(result)
