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

    app.register_blueprint(customer)
    # app.register_blueprint(posts)
    # app.register_blueprint(main)
    # app.register_blueprint(errors)
    
    return app

