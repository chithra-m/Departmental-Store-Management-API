from flask import jsonify, request, make_response
import json, logging

from db_setup import create_app, db
from Services.customer_service import delete_customer_data, get_customer_data, create_customer_data, get_customer_data_by_id, update_customer_data

logging.basicConfig(filename='record.log', level=logging.DEBUG) 

app = create_app()
with app.app_context():
    # db.drop_all() 
    db.create_all()
log = app.logger
log.info('DB tables created')

@app.route("/")
def home():
    return "Hello, Flask!"

#customer
@app.route('/customer',methods=['GET'])
def get_customer():
    try:
        result = get_customer_data(log)
        if result is not None:
            return make_response(jsonify(result), 200)

    except Exception as error:
        log.error("error occurred in app/get_customer" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)

@app.route('/customer/<id>',methods=['GET'])
def get_customer_by_id(id):
    try:
        result = get_customer_data_by_id(id, log)
        if result is not None:
            return make_response(jsonify(result), 200)

    except Exception as error:
       log.error("error occurred in app/get_customer" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)

@app.route('/customer',methods=['POST'])
def create_customer():
    try:
        response = create_customer_data(request.data, log)
        if response:
            if type(response) == type(1):
                return make_response(json.dumps(response), 200)
            return make_response(json.dumps(response), 500)
    except Exception as error:
       log.error("error occurred in app/create_customer" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)

@app.route('/customer',methods=['PUT'])
def update_customer():
    try:
        response = update_customer_data(request.data, log)
        if response:
            if type(response) == type(1):
                return make_response(json.dumps(response), 200)
            return make_response(json.dumps(response), 500)
    except Exception as error:
       log.error("error occurred in app/update_customer" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)

@app.route('/customer/<id>',methods=['DELETE'])
def delete_customer(id):
    try:
        response = delete_customer_data(id, log)
        if response:
            if type(response) == type(1):
                return make_response(json.dumps(response), 200)
            return make_response(json.dumps(response), 500)
    except Exception as error:
       log.error("error occurred in app/delete_customer" + str(error.__class__))

    return make_response(json.dumps("Something went wrong"), 500)


if __name__ == '__main__':
    app.run()
    log.info("app started")