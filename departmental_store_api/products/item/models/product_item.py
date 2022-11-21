from departmental_store_api import db
from departmental_store_api.products.category.model import ProductCategory


class ProductItem(db.Model):
    __tablename__ = 'product_item'
    id = db.Column(db.Integer, primary_key = True)
    name =  db.Column(db.String, nullable = False)
    description = db.Column(db.String)
    product_category_id = db.Column(db.Integer, db.ForeignKey(ProductCategory.id), nullable = False)
    quantity_per_unit = db.Column(db.Integer, nullable = False)
    unit_price = db.Column(db.Integer, nullable = False)
    units_in_stock = db.Column(db.Integer, nullable = False)    
    # orders = db.relationship("Order")

    def __init__(self, name, description, product_category_id, quantity_per_unit, unit_price, units_in_stock) -> None:
        self.name = name 
        self.description = description
        self.product_category_id = product_category_id
        self.quantity_per_unit = quantity_per_unit 
        self.unit_price = unit_price 
        self.units_in_stock = units_in_stock 


