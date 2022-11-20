from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    

    # from flaskauth.users.routes import users
    # from flaskauth.posts.routes import posts
    # from flaskauth.main.routes import main
    # from flaskauth.errors.handlers import errors

    # app.register_blueprint(users)
    # app.register_blueprint(posts)
    # app.register_blueprint(main)
    # app.register_blueprint(errors)
    
    return app

