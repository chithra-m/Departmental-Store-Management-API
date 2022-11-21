from departmental_store_api import db
from departmental_store_api.products.category.model import ProductCategory
from departmental_store_api.products.item.model import ProductItem, ProductItemSchema
import json


def get_item_data(log):
    try:
        temp = ProductItem.query.all()       
        seralizer = ProductItemSchema(many = True)
        data = seralizer.dump(temp)
        return data

    except Exception as error:
        log.error("error occurred in item_service/get_item_data" + str(error.__class__))
        return str(error.__class__)


def get_item_data_by_id(id, log):
    try:
        if id:
            temp = ProductItem.query.filter_by(id = id)        
            seralizer = ProductItemSchema(many = True)
            data = seralizer.dump(temp)
            return data
        
        return "Id is required"

    except Exception as error:
        log.error("error occurred in item_service/get_item_data_by_id" + str(error.__class__))
        return str(error.__class__)


def create_item_data(item, log):
    try:
        if item:
            item = json.loads(item)

            if item['name'] == None or item['name'].isspace():
                return "Name is required"

            exists = db.session.query(db.exists().where(ProductCategory.id == item['product_category_id'])).scalar()

            if not exists:
                return "Invalid category_id"
            
            if item['quantity_per_unit'] == None or item['quantity_per_unit'] <= 0:
                return "quantity_per_unit is required"
            
            if item['unit_price'] == None or item['unit_price'] <= 0:
                return "unit_price is required"

            if item['units_in_stock'] == None or item['units_in_stock'] <= 0:
                return "units_in_stock is required"

            iteminfo = ProductItem(
                name = item['name'],
                description = item['description'],
                product_category_id = item['product_category_id'],
                quantity_per_unit = item['quantity_per_unit'],
                unit_price = item['unit_price'],
                units_in_stock = item['units_in_stock']
            )

            db.session.add(iteminfo)
            db.session.commit()
            return iteminfo.id
            
        return None
    except Exception as error:
        log.error("error occurred in item_service/create_item_data" + str(error.__class__))
        return str(error.__class__)


def update_item_data(update_item, log):
    try:
        if update_item:
            item = json.loads(update_item)

            if item['id'] == None or item['id'] <= 0:
                return "Id is required"

            if item['name'] == None or item['name'].isspace():
                return "Name is required"      

            exists = db.session.query(db.exists().where(ProductCategory.id == item['product_category_id'])).scalar()

            if not exists:
                return "Invalid category_id"
            
            if item['quantity_per_unit'] == None or item['quantity_per_unit'] <= 0:
                return "quantity_per_unit is required"
            
            if item['unit_price'] == None or item['unit_price'] <= 0:
                return "unit_price is required"

            if item['units_in_stock'] == None or item['units_in_stock'] <= 0:
                return "units_in_stock is required"

            exists = db.session.query(db.exists().where(ProductItem.id == item['id'])).scalar()
            if not exists:
                return "Invalid item id"
            item_info = ProductItem.query.get(item['id'])
            item_info.name = item['name']
            item_info.description = item['description']
            item_info.product_category_id = item['product_category_id']
            item_info.quantity_per_unit = item['quantity_per_unit']
            item_info.unit_price = item['unit_price']
            item_info.units_in_stock = item['units_in_stock']

            db.session.commit()
            return item['id']
            
        return None

    except Exception as error:
        log.error("error occurred in item_service/update_item_data" + str(error.__class__))
        return str(error.__class__)


def delete_item_data(item_id, log):
    try:
        if not item_id:
            return "item_id is required"
        
        item_id = int(item_id)

        if item_id <= 0:
            return "item_id is invalid"

        exists = db.session.query(db.exists().where(ProductItem.id == item_id)).scalar()
        if exists:
            db.session.delete(ProductItem.query.get(item_id))
            db.session.commit()
            return item_id

        return "ProductItem data not available"

    except Exception as error:
        log.error("error occurred in item_service/delete_item_data" + str(error.__class__))
        return str(error.__class__)
