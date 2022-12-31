from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# create connection point to db as db obj
db = SQLAlchemy()
# compare_type allows you to detect changes in dtype in migrations
migrate = Migrate(compare_type=True)
# load .env variables
load_dotenv()

def create_app(test_config=None):
    """
    Start-up logic for Flask API
    :params: 
    - test_config (bool): flag for test/development mode
    """
    app = Flask(__name__)
    # Turn off SQLAlchemy event sys to save sys resources
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # connect to db
    if not test_config:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DB_URI")
    else:
        # turn testing mode on
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_TEST_DB_URI")
    # connect db & migrate objs to Flask app
    db.init_app(app)
    migrate.init_app(app, db)
    # import has to happen after db initialized
    from app.models.book import Book
    # register blueprint group's related endpoints
    from app.routes.books import books_bp
    app.register_blueprint(books_bp)
    return app
