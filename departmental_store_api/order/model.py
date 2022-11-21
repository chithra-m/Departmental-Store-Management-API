from datetime import datetime, timedelta
from departmental_store_api import db
from marshmallow import Schema, fields

order_product = db.Table('order_product',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product_item.id'), primary_key=True)
)

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key = True)
    # quantity = db.Column(db.Integer, nullable = False) #todo move to product_purchase tbl
    amount = db.Column(db.Integer, nullable = False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)    
    products = db.relationship('ProductItem', secondary=order_product)

    def __init__(self, amount, customer_id, order_date = datetime.utcnow, products = []) -> None:
        # self.quantity = quantity
        self.amount = amount
        self.order_date = order_date
        self.customer_id = customer_id
        self.products = products


class OrderSchema(Schema):
    id = fields.Integer()
    # quantity =  fields.Integer()
    amount = fields.Integer()
    order_date = fields.DateTime()
    customer_id = fields.Integer()
    products = fields.List(
        fields.Nested(lambda: ProductItemSchema())
    )

class ProductItemSchema(Schema):
    id = fields.Integer()
    name =  fields.String()
    description = fields.String()
    product_category_id = fields.Integer()
    quantity_per_unit = fields.Integer()
    unit_price = fields.Integer()
    units_in_stock = fields.Integer()
    order = fields.Nested(lambda: OrderSchema(only=("id",)), dump_only=True)