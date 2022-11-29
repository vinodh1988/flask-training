from config import app,db
#from database import Person
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

#Patch is for partial updation , in a given resource if you partially update database
#Put , if you completely update the record or replace record without changing the id
@app.route('/people/<int:sno>',methods=['PUT','PATCH'])
def updatePeople(sno):
    try:
        person=Person.query.get(sno)
        if(person):
             input=request.get_json()
             if('name' in input.keys()):
                person.name=input['name']
             if('city' in input.keys()):
                person.city=input['city']
             db.session.commit()
        else:
            raise Exception("No such sno");
        return {"Status": "successfully update"}, 200
    except Exception as e:
        
        return {"Status": "Not updated- May be id not exists"}, 500

@app.route('/people/<int:sno>',methods=['delete'])
def deletePeople(sno):
    try:
        person=Person.query.get(sno)
        if(person):
             db.session.delete(person)
             db.session.commit()
        else:
            raise Exception("No such sno");
        return {"Status": "successfully update"}, 200
    except Exception as e:
        print(e)
        return {"Status": "Not updated- May be id not exists"}, 500



