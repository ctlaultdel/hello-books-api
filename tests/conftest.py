import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.book import Book

# way to configure global variables for use in test_routes
def pytest_configure():
    pytest.ocean_book = Book(title="Ocean Book", description="watr 4evr")
    pytest.mountain_book = Book(title="Mountain Book", description="i luv 2 climb rocks",)

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        # creates new session to see if changes persist in db
        db.session.remove()
    
    with app.app_context():
        # recreates tables needed for models
        db.create_all()
        # stop here until tests finish running
        yield app
    
    with app.app_context():
        # drop all tables created during tests
        db.drop_all()

# create two books for testing get book by id
@pytest.fixture
def two_saved_books(app):
    # Arrange
    db.session.add_all([pytest.ocean_book, pytest.mountain_book])
    # commits & saves books to db
    db.session.commit()

# create test client for making HTTP requests
@pytest.fixture
def client(app):
    return app.test_client()