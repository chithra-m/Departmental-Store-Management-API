from departmental_store_api import db
from departmental_store_api.customer.model import Customer, CustomerSchema
import json

def get_customer_data(log):
    try:
        temp = Customer.query.all()       
        seralizer = CustomerSchema(many = True)
        data = seralizer.dump(temp)
        return data

    except Exception as error:
        log.error("error occurred in customer_service/get_customer_data" + str(error.__class__))
        return str(error.__class__)

def get_customer_data_by_id(id, log):
    try:
        if id:
            temp = Customer.query.filter_by(id = id)        
            seralizer = CustomerSchema(many = True)
            data = seralizer.dump(temp)
            return data
        
        return "Id is required"

    except Exception as error:
        log.error("error occurred in customer_service/get_customer_data_by_id" + str(error.__class__))
        return str(error.__class__)

def create_customer_data(customer, log):
    try:
        if customer:
            customer = json.loads(customer)

            if customer['name'] == None or customer['name'].isspace():
                return "Name is required"

            if customer['email'] == None or customer['email'].isspace():
                return "Email is required"

            if customer['contactno'] == None or customer['contactno'].isspace():
                return "Contactno is required"

            customerinfo = Customer(
                name = customer['name'],
                email = customer['email'],
                contactno = customer['contactno'],
                address = customer['address']
            )

            db.session.add(customerinfo)
            db.session.commit()
            return customerinfo.id
            
        return None
    except Exception as error:
        log.error("error occurred in customer_service/create_customer_data" + str(error.__class__))
        return str(error.__class__)

def update_customer_data(update_customer, log):
    try:
        if update_customer:
            customer = json.loads(update_customer)

            if customer['id'] == None or customer['id'] <= 0:
                return "Id is required"

            if customer['name'] == None or customer['name'].isspace():
                return "Name is required"

            if customer['email'] == None or customer['email'].isspace():
                return "Email is required"

            if customer['contactno'] == None or customer['contactno'].isspace():
                return "Contactno is required"            

            if customer['address'] == None or customer['address'].isspace():
                return "Address is required"            

            customer_info = Customer.query.get(customer['id'])
            customer_info.name = customer['name']
            customer_info.email = customer['email']
            customer_info.contactno = customer['contactno']
            customer_info.address = customer['address']

            db.session.commit()
            return customer['id']
            
        return None

    except Exception as error:
        log.error("error occurred in customer_service/update_customer_data" + str(error.__class__))
        return str(error.__class__)

def delete_customer_data(customer_id, log):
    try:
        if not customer_id:
            return "customer_id is required"
        
        customer_id = int(customer_id)

        if customer_id <= 0:
            return "customer_id is invalid"

        exists = db.session.query(db.exists().where(Customer.id == customer_id)).scalar()
        if exists:
            db.session.delete(Customer.query.get(customer_id))
            db.session.commit()
            return customer_id

        return "Customer data not available"

    except Exception as error:
        log.error("error occurred in customer_service/delete_customer_data" + str(error.__class__))
        return str(error.__class__)
