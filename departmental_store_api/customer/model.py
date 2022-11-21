from departmental_store_api import db
from sqlalchemy.orm import relationship, backref 
from marshmallow import Schema, fields

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False, unique = True)
    contact_no = db.Column(db.String, nullable = False)
    address = db.Column(db.String)

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