from departmental_store_api import create_app, db
import logging

logging.basicConfig(filename='record.log', level=logging.DEBUG) 

app = create_app()
with app.app_context():
    # db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run()