import json
from flask import Blueprint, jsonify, make_response, request
from departmental_store_api.order.service import *
import logging

order = Blueprint('order', __name__)

#order
@order.route('/order',methods=['GET'])
def get_order():
    try:
        result = get_order_data()
        if result is not None:
            return make_response(jsonify(result), 200)

    except Exception as error:
        logging.error("error occurred in order/get_order" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)

@order.route('/order/<id>',methods=['GET'])
def get_order_by_id(id):
    try:
        result = get_order_data_by_id(id)
        if result is not None:
            return make_response(jsonify(result), 200)

    except Exception as error:
       logging.error("error occurred in order/get_order_by_id" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)

@order.route('/order',methods=['POST'])
def create_order():
    try:
        response = create_order_data(request.data)
        if response:
            if isinstance(response, int):
                return make_response(json.dumps(response), 200)
            return make_response(json.dumps(response), 500)
    except Exception as error:
       logging.error("error occurred in order/create_order" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)

@order.route('/order/<id>',methods=['DELETE'])
def delete_order(id):
    try:
        response = delete_order_data(id)
        if response:
            if isinstance(response, int):
                return make_response(json.dumps(response), 200)
            return make_response(json.dumps(response), 500)
    except Exception as error:
       logging.error("error occurred in order/delete_order" + str(error.__class__))

    return make_response(json.dumps("Something went wrong"), 500)