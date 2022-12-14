# start-up logic for Flask API
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)

    return app
