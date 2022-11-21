from departmental_store_api import db
from departmental_store_api.products.item.model import ProductItem, ProductItemSchema
from marshmallow import Schema, fields

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    contact_no = db.Column(db.String)
    # items = db.relationship("Items", secondary="item_supplier", back_populates='supplier')

    def __init__(self, name, contact_no) -> None:
        self.name = name 
        self.contact_no = contact_no 
      

class SupplierSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    contact_no = fields.String()

    # items = fields.Nested(ProductItemSchema, many=True)


# item_supplier = db.Table('item_supplier',
#     db.Column("id", db.Integer, primary_key = True),
#     db.Column("item_id", db.Integer, db.ForeignKey(ProductItem.id)),
#     db.Column("supplier_id", db.Integer, db.ForeignKey(Supplier.id))
# )


