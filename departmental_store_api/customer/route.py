import json
from flask import Blueprint, jsonify, make_response, request
from departmental_store_api.customer.service import *
import logging

customer = Blueprint('customer', __name__)

@customer.route('/customer',methods=['GET'])
def get_customer():
    try:
        result = get_customer_data()
        if result is not None:
            return make_response(jsonify(result), 200)

    except Exception as error:
        logging.error("error occurred in customer/get_customer" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)


@customer.route('/customer/<id>',methods=['GET'])
def get_customer_by_id(id):
    try:
        result = get_customer_data_by_id(id)
        if result is not None:
            return make_response(jsonify(result), 200)

    except Exception as error:
       logging.error("error occurred in customer/get_customer" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)


@customer.route('/customer',methods=['POST'])
def create_customer():
    try:
        response = create_customer_data(request.data)
        if response:
            if isinstance(response, int):
                return make_response(json.dumps(response), 200)
            return make_response(json.dumps(response), 500)
    except Exception as error:
       logging.error("error occurred in customer/create_customer" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)


@customer.route('/customer',methods=['PUT'])
def update_customer():
    try:
        response = update_customer_data(request.data)
        if response:
            if isinstance(response, int):
                return make_response(json.dumps(response), 200)
            return make_response(json.dumps(response), 500)
    except Exception as error:
       logging.error("error occurred in customer/update_customer" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)


@customer.route('/customer/<id>',methods=['DELETE'])
def delete_customer(id):
    try:
        response = delete_customer_data(id)
        if response:
            if isinstance(response, int):
                return make_response(json.dumps(response), 200)
            return make_response(json.dumps(response), 500)
    except Exception as error:
       logging.error("error occurred in customer/delete_customer" + str(error.__class__))

    return make_response(json.dumps("Something went wrong"), 500)