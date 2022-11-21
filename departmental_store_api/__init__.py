from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from departmental_store_api.config import Config
import logging

db = SQLAlchemy()
logging.basicConfig(filename='record.log', level=logging.DEBUG) 
log = None

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    log = app.logger
    log.info('DB tables created')

    from departmental_store_api.customer.route import customer
    from departmental_store_api.products.category.route import category
    from departmental_store_api.products.item.route import item
    from departmental_store_api.supplier.route import supplier
    from departmental_store_api.order.route import order

    app.register_blueprint(customer)
    app.register_blueprint(category)
    app.register_blueprint(item)
    app.register_blueprint(supplier)
    app.register_blueprint(order)
    
    return app

