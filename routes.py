from app import app 
from service import getUserData, postUserData,  putUser, deleteUser
from flask import request

@app.route("/")
def home():
    app.logger.info("home page")
    return "Hello, Flask!"

@app.route('/user',methods=['GET'])
@app.route('/user/<id>',methods=['GET'])
def read_user(id=None):
    app.logger.info("user api")
    return getUserData(id)

@app.route('/user',methods=['POST'])
def insert_user():
    return postUserData(request.data)

@app.route('/user',methods=['PUT'])
def update_user():
    return putUser(request.data)

@app.route('/user/<id>',methods=['DELETE'])
def delete_user(id):
    return deleteUser(id)
