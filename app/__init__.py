from flask import Flask

# start-up logic for Flask API
def create_app(test_config=None):
    app = Flask(__name__)

    
    from app.routes.hello_world import hello_world_bp
    from app.routes.books import books_bp
    # register the hello_world_bp Blueprint
    # i.e. tell app to use the following endpoints for its routing
    app.register_blueprint(hello_world_bp)
    app.register_blueprint(books_bp)

    return app
