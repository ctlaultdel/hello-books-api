import pytest
from app import create_app
from app import db
from flask.signals import request_finished

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

# create test client for making HTTP requests
@pytest.fixture
def client(app):
    return app.test_client()