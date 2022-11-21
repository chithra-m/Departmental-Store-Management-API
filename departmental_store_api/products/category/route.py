import json
from flask import Blueprint, jsonify, make_response, request
from departmental_store_api.products.category.service import get_category_data, create_category_data, delete_category_data, get_category_data_by_id, update_category_data
import logging 

category = Blueprint('category', __name__)

#category
@category.route('/category',methods=['GET'])
def get_category():
    try:
        result = get_category_data()
        if result is not None:
            return make_response(jsonify(result), 200)

    except Exception as error:
        logging.error("error occurred in category/get_category" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)


@category.route('/category/<id>',methods=['GET'])
def get_category_by_id(id):
    try:
        result = get_category_data_by_id(id)
        if result is not None:
            return make_response(jsonify(result), 200)

    except Exception as error:
       logging.error("error occurred in category/get_category" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)


@category.route('/category',methods=['POST'])
def create_category():
    try:
        response = create_category_data(request.data)
        if response:
            if type(response) == type(1):
                return make_response(json.dumps(response), 200)
            return make_response(json.dumps(response), 500)
    except Exception as error:
       logging.error("error occurred in category/create_category" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)


@category.route('/category',methods=['PUT'])
def update_category():
    try:
        response = update_category_data(request.data)
        if response:
            if type(response) == type(1):
                return make_response(json.dumps(response), 200)
            return make_response(json.dumps(response), 500)
    except Exception as error:
       logging.error("error occurred in category/update_category" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)


@category.route('/category/<id>',methods=['DELETE'])
def delete_category(id):
    try:
        response = delete_category_data(id)
        if response:
            if type(response) == type(1):
                return make_response(json.dumps(response), 200)
            return make_response(json.dumps(response), 500)
    except Exception as error:
       logging.error("error occurred in category/delete_category" + str(error.__class__))   

    return make_response(json.dumps("Something went wrong"), 500)