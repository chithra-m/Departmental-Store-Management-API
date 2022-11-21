#NOTE Due to Circular reference moved to Order model class

# from marshmallow import Schema, fields
# from departmental_store_api.order.model import OrderSchema


# class ProductItemSchema(Schema):
#     id = fields.Integer()
#     name =  fields.String()
#     description = fields.String()
#     product_category_id = fields.Integer()
#     quantity_per_unit = fields.Integer()
#     unit_price = fields.Integer()
#     units_in_stock = fields.Integer()
#     order = fields.Nested(lambda: OrderSchema(only=("id",)), dump_only=True)