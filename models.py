from db_setup import db
from datetime import datetime 
from sqlalchemy.orm import relationship, backref 
from marshmallow import Schema, fields

class Response:
    data = None
    is_success = False
    status_message = 'Failed'
    validation_error_message = []

    def __init__(self, data = None) -> None:
        self.data = data
        self.is_success = data is not None
        self.status_message = 'Success' if data is not None else 'Failed'
        self.validation_error_message = []

    def getFailedResponse():
        return Response()
    
class ResponseSchema(Schema):
    data = fields.Raw(required=True)
    is_success = False
    status_message = 'Failed'
    validation_error_message = []

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False, unique = True)
    contactno = db.Column(db.BigInteger, nullable = False)

    def __init__(self, id, name, email, contactno):
        self.id = id
        self.name = name
        self.email = email
        self.contactno = contactno

class UsersSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    email = fields.String()
    contactno = fields.String()

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False, unique = True)
    contact_no = db.Column(db.String, nullable = False)
    address = db.Column(db.String)
    # address_id = db.Column(db.Integer,db.ForeignKey('address.id'))

    def __init__(self, name, email, contactno, address):
        self.name = name
        self.email = email
        self.contact_no = contactno
        self.address = address

class CustomerSchema(Schema):
    id = fields.Integer()
    name =  fields.String()
    email = fields.String()
    contact_no = fields.String()
    address = fields.String()


# class Category(db.Model):
#     category_id = db.Column(db.Integer, primary_key = True)
#     category_name = db.Column(db.String, nullable = False)
#     category_description = db.Column(db.String)
#     items = db.relationship("Items", backref = "category")

#     def __init__(self, category_id, category_name, category_description) -> None:
#         self.category_id = category_id
#         self.category_name = category_name 
#         self.category_description = category_description 


# class Items(db.Model):
#     item_id = db.Column(db.Integer, primary_key = True)
#     item_name =  db.Column(db.String, nullable = False)
#     # supplier_id = db.Column(db.Integer, db.ForeignKey("supplier.supplier_id") , nullable = False)
#     category_id = db.Column(db.Integer, db.ForeignKey("category.category_id"), nullable = False)
#     quantity_per_unit = db.Column(db.String, nullable = False)
#     unit_price = db.Column(db.Integer, nullable = False)
#     units_in_stock = db.Column(db.Integer, nullable = False)
#     audit_created_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     audit_updated_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
#     # items = db.relationship("Category", backref = "items")
#     categories = relationship('Category', secondary="item_supplier")

#     def __init__(self, item_id, item_name, supplier_id, category_id, quantity_per_unit, unit_price, units_in_stock) -> None:
#         self.item_id = item_id
#         self.item_name = item_name 
#         self.supplier_id = supplier_id
#         self.category_id = category_id
#         self.quantity_per_unit = quantity_per_unit 
#         self.unit_price = unit_price 
#         self.units_in_stock = units_in_stock 


# class Order(db.Table):
#     id = db.Column(db.Integer, primary_key=True) 
#     customer_id =  db.Column(db.Integer, db.ForeignKey('Customer.customer_id'))
#     item_id = db.Column(db.Integer, db.ForeignKey('Items.item_id'))
#     order_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

#     customer = relationship(Customer, backref = backref("Customer", cascade="all, delete-orphan"))
#     item = relationship(Items, backref = backref("Items", cascade="all, delete-orphan"))


# class Supplier(db.Model):
#     supplier_id = db.Column(db.Integer, primary_key = True)
#     supplier_name = db.Column(db.String, nullable = False)
#     address_id = db.Column(db.Integer)

#     items = relationship("Items", secondary="item_supplier", back_populates='supplier')


# class Item_supplier(db.Table):
#     __tablename__ = 'item_supplier'
#     item_id = db.Column(db.Integer, db.ForeignKey(Items.item_id), primary_key = True)
#     supplier_ = db.Column(db.Integer, db.ForeignKey(Supplier.supplier_id), primary_key = True)


# item_supplier = db.Table('item_supplier',
#     # db.Column('item_id', db.Integer, db.ForeignKey('Items.item_id'), primary_key=True),
#     # db.Column('supplier_id', db.Integer, db.ForeignKey('Supplier.supplier_id'), primary_key=True)
#     db.Column('item_id', db.Integer, db.ForeignKey(Items.item_id), primary_key=True),
#     db.Column('supplier_id', db.Integer, db.ForeignKey(Supplier.supplier_id), primary_key=True)
# )


# class Address(db.Model):
#     address_id = db.Column(db.Integer, primary_key = True)
#     address = db.Column(db.String, nullable = False)
#     city = db.Column(db.String)
#     state = db.Column(db.String)  
#     country = db.Column(db.String)
#     postal_code = db.Column(db.Integer)



