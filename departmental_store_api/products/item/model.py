from departmental_store_api import db
from marshmallow import Schema, fields
from departmental_store_api.products.category.model import ProductCategory
from datetime import datetime


class ProductItem(db.Model):
    __tablename__ = 'product_item'
    id = db.Column(db.Integer, primary_key = True)
    name =  db.Column(db.String, nullable = False)
    description = db.Column(db.String)
    # supplier_id = db.Column(db.Integer, db.ForeignKey("supplier.supplier_id") , nullable = False)
    product_category_id = db.Column(db.Integer, db.ForeignKey(ProductCategory.id), nullable = False)
    quantity_per_unit = db.Column(db.String, nullable = False)
    unit_price = db.Column(db.Integer, nullable = False)
    units_in_stock = db.Column(db.Integer, nullable = False)
    # audit_created_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # audit_updated_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # items = db.relationship("Category", backref = "items")
    # categories = relationship('Category', secondary="supplier")

    def __init__(self, name, description, product_category_id, quantity_per_unit, unit_price, units_in_stock) -> None:
        self.name = name 
        self.description = description
        # self.supplier_id = supplier_id
        self.product_category_id = product_category_id
        self.quantity_per_unit = quantity_per_unit 
        self.unit_price = unit_price 
        self.units_in_stock = units_in_stock 


class ProductItemSchema(Schema):
    id = fields.Integer()
    name =  fields.String()
    description = fields.String()
    product_category_id = fields.Integer()
    quantity_per_unit = fields.Integer()
    unit_price = fields.Integer()
    units_in_stock = fields.Integer()