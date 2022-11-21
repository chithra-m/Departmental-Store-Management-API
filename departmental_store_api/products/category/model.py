from departmental_store_api import db
from marshmallow import Schema, fields
from sqlalchemy.orm import relationship
# from departmental_store_api.products.item.model import ProductItem

class ProductCategory(db.Model):
    __tablename__ = 'product_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False, unique = True)
    description = db.Column(db.String)
    product_item = relationship("ProductItem", backref = "ProductCategory")

    def __init__(self, name, description):
        self.name = name
        self.description = description

class ProductCategorySchema(Schema):
    id = fields.Integer()
    name =  fields.String()
    description = fields.String()