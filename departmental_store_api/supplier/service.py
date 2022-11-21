from departmental_store_api import db
from departmental_store_api.supplier.model import Supplier, SupplierSchema

import json
import logging


def get_supplier_data():
    try:
        temp = Supplier.query.all()       
        seralizer = SupplierSchema(many = True)
        data = seralizer.dump(temp)
        return data
    
    except Exception as error:
        logging.error("error occurred in supplier_service/get_supplier_data" + str(error.__class__))
        return str(error.__class__)


def get_supplier_data_by_id(id):
    try:
        if id:
            temp = Supplier.query.filter_by(id = id)        
            seralizer = SupplierSchema(many = True)
            data = seralizer.dump(temp)
            return data
        
        return "Id is required"

    except Exception as error:
        logging.error("error occurred in supplier_service/get_supplier_data_by_id" + str(error.__class__))
        return str(error.__class__)


def create_supplier_data(supplier):
    try:
        if supplier:
            supplier = json.loads(supplier)

            if supplier['name'] == None or supplier['name'].isspace():
                return "Name is required"

            supplierinfo = Supplier(
                name = supplier['name'],
                contact_no = supplier["contact_no"]
            )

            db.session.add(supplierinfo)
            db.session.commit()
            return supplierinfo.id
            
        return None
    except Exception as error:
        logging.error("error occurred in supplier_service/create_supplier_data" + str(error.__class__))
        return str(error.__class__)


def update_supplier_data(update_supplier):
    try:
        if update_supplier:
            supplier = json.loads(update_supplier)

            if supplier['id'] == None or supplier['id'] <= 0:
                return "Id is required"

            if supplier['name'] == None or supplier['name'].isspace():
                return "Name is required"      

            supplier_info = Supplier.query.get(supplier['id'])
            
            if supplier_info:
                supplier_info.name = supplier['name']
                supplier_info.contact_no = supplier["contact_no"]

                db.session.commit()
                return supplier['id']
            
        return None

    except Exception as error:
        logging.error("error occurred in supplier_service/update_supplier_data" + str(error.__class__))
        return str(error.__class__)


def delete_supplier_data(supplier_id):
    try:
        if not supplier_id:
            return "supplier_id is required"
        
        supplier_id = int(supplier_id)

        if supplier_id <= 0:
            return "supplier_id is invalid"

        # exists = db.session.query(db.exists().where(Supplier.id == supplier_id)).scalar()
        # if exists:
        #     exists = db.session.query(db.exists().where(ProductItem.id == supplier_id)).scalar()
            
        #     if exists:
        #         logging.error("error occurred in supplier_service/delete_supplier_data  -> Table reference error, supplier_id is {supplier_id}")
        #         return "Table reference error"

        db.session.delete(Supplier.query.get(supplier_id))
        db.session.commit()
        return supplier_id

        return "Supplier data not available"

    except Exception as error:
        logging.error("error occurred in supplier_service/delete_supplier_data" + str(error.__class__))
        return str(error.__class__)
