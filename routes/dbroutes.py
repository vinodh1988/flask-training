from config import app,db
from database import Person
from flask import jsonify,request,abort

@app.route('/people')
def getPeople():
    listp=Person.query.all()
    result=[ x.serialize() for x in listp]
    return jsonify(result)

@app.route('/people',methods=['post'])
def addPeople():
    try:
        input=request.get_json()
        sno=input['sno']
        name=input['name']
        city=input['city']
        db.session.add(Person(sno,name,city))
        db.session.commit()
        return {"status":"success"}, 201
    except:
        abort ( {"status": "Server error"}, 500)
