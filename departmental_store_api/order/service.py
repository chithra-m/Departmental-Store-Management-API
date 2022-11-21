import datetime
import json
from departmental_store_api import db
from departmental_store_api.order.model import Order, OrderSchema
import logging

from departmental_store_api.products.item.models.product_item import ProductItem

def get_order_data():
    try:
        temp = Order.query.all()       
        seralizer = OrderSchema(many = True)
        data = seralizer.dump(temp)
        return data

    except Exception as error:
        logging.error("error occurred in order_service/get_order_data" + str(error.__class__))
        return str(error.__class__)

def get_order_data_by_id(id):
    try:
        if id:
            temp = Order.query.filter_by(id = id)        
            seralizer = OrderSchema(many = True)
            data = seralizer.dump(temp)
            return data

        return "Id is required"

    except Exception as error:
        logging.error("error occurred in order_service/get_order_data_by_id" + str(error.__class__))
        return str(error.__class__)

def create_order_data(order):
    try:
        if order:
            order = json.loads(order)
            product_items_list = list(order['products'])
            product_details_list = db.session.query(ProductItem).filter(ProductItem.id.in_(product_items_list)).all()            
            total_amount = sum([pdt.unit_price for pdt in product_details_list])

            orderinfo = Order(
                amount = total_amount,
                order_date = datetime.datetime.now(),
                order_id = order['order_id'],
                products=product_details_list
            )
            
            db.session.add(orderinfo)
            db.session.commit()
            return orderinfo.id
            
        return None
    except Exception as error:
        logging.error("error occurred in order_service/create_order_data" + str(error.__class__))
        return str(error.__class__)

def delete_order_data(order_id):
    try:
        if not order_id:
            return "order_id is required"
        
        order_id = int(order_id)

        if order_id <= 0:
            return "order_id is invalid"

        exists = db.session.query(db.exists().where(Order.id == order_id)).scalar()
        if exists:
            db.session.delete(Order.query.get(order_id))
            db.session.commit()
            return order_id

        return "Order data not available"

    except Exception as error:
        logging.error("error occurred in order_service/delete_order_data" + str(error.__class__))
        return str(error.__class__)