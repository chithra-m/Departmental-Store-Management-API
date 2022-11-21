from departmental_store_api import db
from marshmallow import Schema, fields

class ProductItem(db.Model):
    __tablename__ = 'product_item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False, unique = True)
    product_category_id = db.Column(db.Integer, db.ForeignKey("product_category.id"))


    def __init__(self, name, description):
        self.name = name
        self.description = description

class ProductItemSchema(Schema):
    id = fields.Integer()
    name =  fields.String()