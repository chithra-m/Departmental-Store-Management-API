import json
from flask import Blueprint, jsonify, make_response, request
from departmental_store_api.supplier.service import get_supplier_data, get_supplier_data_by_id, create_supplier_data, update_supplier_data, delete_supplier_data
import logging

supplier = Blueprint('supplier', __name__)

#Supplier
@supplier.route('/supplier',methods=['GET'])
def get_Supplier():
    try:
        result = get_supplier_data()
        if result is not None:
            return make_response(jsonify(result), 200)

    except Exception as error:
        logging.error("error occurred in Supplier/get_Supplier" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)


@supplier.route('/supplier/<id>',methods=['GET'])
def get_Supplier_by_id(id):
    try:
        result = get_supplier_data_by_id(id)
        if result is not None:
            return make_response(jsonify(result), 200)

    except Exception as error:
       logging.error("error occurred in Supplier/get_Supplier" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)


@supplier.route('/supplier',methods=['POST'])
def create_Supplier():
    try:
        response = create_supplier_data(request.data)
        if response:
            if isinstance(response, int):
                return make_response(json.dumps(response), 200)
            return make_response(json.dumps(response), 500)
    except Exception as error:
       logging.error("error occurred in Supplier/create_Supplier" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)


@supplier.route('/supplier',methods=['PUT'])
def update_Supplier():
    try:
        response = update_supplier_data(request.data)
        if response:
            if isinstance(response, int):
                return make_response(json.dumps(response), 200)
            return make_response(json.dumps(response), 500)
    except Exception as error:
       logging.error("error occurred in Supplier/update_Supplier" + str(error.__class__))
        
    return make_response(json.dumps("Something went wrong"), 500)


@supplier.route('/supplier/<id>',methods=['DELETE'])
def delete_Supplier(id):
    try:
        response = delete_supplier_data(id)
        if response:
            if isinstance(response, int):
                return make_response(json.dumps(response), 200)
            return make_response(json.dumps(response), 500)
    except Exception as error:
       logging.error("error occurred in Supplier/delete_Supplier" + str(error.__class__))

    return make_response(json.dumps("Something went wrong"), 500)