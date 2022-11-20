from db_setup import db
from models import Users
import json


def getUserData(id):
    try:
        if id:
            result = Users.query.filter_by(id = id)
        else:
            result = Users.query.all()
        
        res = {}
        index = 0
        
        for user in result:    
            temp = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'contactno': user.contactno           
            }
            res[index] =  temp
            index += 1
        return res
        
    except Exception as error:
        res = {"error occurred" : str(error.__class__)}
        # logger.error(res)
        print("res", res)
        return res


def postUserData(data):
    try:
        data = json.loads(data)
        if isinstance(data,dict):
            data = [data]
        
        print("data", data)
        for user in data:
            print("user", user, user['id'])    
            db.session.add(Users(
                id = user['id'],
                name = user['name'],
                email = user['email'],
                contactno = user['contactno']
            ))

        db.session.commit()
        # return json.dumps(response)
        return "Inserted Successfully"

    except Exception as error:
        res = {"error occurred":str(error.__class__)}
        return res
      

# def postUser(data):
#     try:
#         print(data)
#         data = json.loads(data)
#         if isinstance(data,dict):
#             data = [data]        
#         response = postUserData(data)
#         print("response", response)
#         return json.dumps(response)
#     except Exception as error:
#         res = {"error occurred":str(error.__class__)}
#         return json.dumps(res)


def putUserData(data):
    for user in data:
        updateUser = Users.query.get(user['id'])
        print(updateUser.name)
        updateUser.name = user['name']
        updateUser.email = user['email']
        updateUser.contactno = user['contactno']
        print(updateUser.name)
    db.session.commit()
    return "Updated Successfully"


def putUser(data):
    try:
        data = json.loads(data)
        if isinstance(data,dict):
            data = [data]
        for user in data:
            updateUser = Users.query.get(user['id'])
            print(updateUser.name)
            updateUser.name = user['name']
            updateUser.email = user['email']
            updateUser.contactno = user['contactno']
            print(updateUser.name)
        db.session.commit()
        return "Updated Successfully"
        
    except Exception as error:
        res = {"error occurred" : str(error.__class__)}
        return json.dumps(res)


def deleteUser(id = None):
    try:
        if not id:
            raise Exception("id is required")
        # checking whether the user id exists, scalar -> will give the first result. if no result, then None
        exists = db.session.query(db.exists().where(Users.id == 'id')).scalar()
        if exists:
            db.session.delete(Users.query.get(id))
            db.session.commit()
            return "Deleted Successfully"     
        else:
            return "User id not available"

    except Exception as error:
        res = {"error occurred" : str(error.__class__)}
        return json.dumps(res)
    


    