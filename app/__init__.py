from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# connection string for finding db
c_str = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

# create connection point to db as db obj
db = SQLAlchemy()
# compare_type allows you to detect changes in dtype in migrations
migrate = Migrate(compare_type=True)

def create_app(test_config=None):
    """
    Start-up logic for Flask API
    """
    app = Flask(__name__)
    # Turn off SQLAlchemy event sys to save sys resources
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # connect to db using connection string
    app.config['SQLALCHEMY_DATABASE_URI'] = c_str
    # connect db & migrate objs to Flask app
    db.init_app(app)
    migrate.init_app(app, db)
    # import has to happen after db initialized
    from app.models.book import Book
    # register blueprint group's related endpoints
    from app.routes.books import books_bp
    app.register_blueprint(books_bp)
    return app
