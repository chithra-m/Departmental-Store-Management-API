import json
from flask import Blueprint, jsonify, make_response, request
from departmental_store_api.products.item.service import *
import logging

item = Blueprint('item', __name__)

#item
@item.route('/item',methods=['GET'])
def get_item():
    try:
        result = get_item_data()
        if result is not None:
            return make_response(jsonify(result), 200)

    except Exception as error:
        logging.error("error occurred in item/get_item" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)


@item.route('/item/<id>',methods=['GET'])
def get_item_by_id(id):
    try:
        result = get_item_data_by_id(id)
        if result is not None:
            return make_response(jsonify(result), 200)

    except Exception as error:
       logging.error("error occurred in item/get_item_by_id" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)


@item.route('/item',methods=['POST'])
def create_item():
    try:
        response = create_item_data(request.data)
        if response:
            if isinstance(response, int):
                return make_response(json.dumps(response), 200)
            return make_response(json.dumps(response), 500)
    except Exception as error:
       logging.error("error occurred in item/create_item" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)


@item.route('/item',methods=['PUT'])
def update_item():
    try:
        response = update_item_data(request.data)
        if response:
            if isinstance(response, int):
                return make_response(json.dumps(response), 200)
            return make_response(json.dumps(response), 500)
    except Exception as error:
       logging.error("error occurred in item/update_item" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)


@item.route('/item/<id>',methods=['DELETE'])
def delete_item(id):
    try:
        response = delete_item_data(id)
        if response:
            if isinstance(response, int):
                return make_response(json.dumps(response), 200)
            return make_response(json.dumps(response), 500)
    except Exception as error:
       logging.error("error occurred in item/delete_item" + str(error.__class__))

    return make_response(json.dumps("Something went wrong"), 500)