from departmental_store_api import db
from departmental_store_api.products.category.model import ProductCategory, ProductCategorySchema
import json

def get_category_data(log):
    try:
        temp = ProductCategory.query.all()       
        seralizer = ProductCategorySchema(many = True)
        data = seralizer.dump(temp)
        return data

    except Exception as error:
        log.error("error occurred in category_service/get_category_data" + str(error.__class__))
        return str(error.__class__)

def get_category_data_by_id(id, log):
    try:
        if id:
            temp = ProductCategory.query.filter_by(id = id)        
            seralizer = ProductCategorySchema(many = True)
            data = seralizer.dump(temp)
            return data
        
        return "Id is required"

    except Exception as error:
        log.error("error occurred in category_service/get_category_data_by_id" + str(error.__class__))
        return str(error.__class__)

def create_category_data(category, log):
    try:
        if category:
            category = json.loads(category)

            if category['name'] == None or category['name'].isspace():
                return "Name is required"

            categoryinfo = ProductCategory(
                name = category['name'],
                description = category['description']
            )

            db.session.add(categoryinfo)
            db.session.commit()
            return categoryinfo.id
            
        return None
    except Exception as error:
        log.error("error occurred in category_service/create_category_data" + str(error.__class__))
        return str(error.__class__)

def update_category_data(update_category, log):
    try:
        if update_category:
            category = json.loads(update_category)

            if category['id'] == None or category['id'] <= 0:
                return "Id is required"

            if category['name'] == None or category['name'].isspace():
                return "Name is required"      

            category_info = ProductCategory.query.get(category['id'])
            category_info.name = category['name']
            category_info.description = category['description']

            db.session.commit()
            return category['id']
            
        return None

    except Exception as error:
        log.error("error occurred in category_service/update_category_data" + str(error.__class__))
        return str(error.__class__)

def delete_category_data(category_id, log):
    try:
        if not category_id:
            return "category_id is required"
        
        category_id = int(category_id)

        if category_id <= 0:
            return "category_id is invalid"

        exists = db.session.query(db.exists().where(ProductCategory.id == category_id)).scalar()
        if exists:
            db.session.delete(ProductCategory.query.get(category_id))
            db.session.commit()
            return category_id

        return "ProductCategory data not available"

    except Exception as error:
        log.error("error occurred in category_service/delete_category_data" + str(error.__class__))
        return str(error.__class__)
