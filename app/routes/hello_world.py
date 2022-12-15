from flask import Blueprint

# store Blueprint instances
# name convention: name related to data being served or functionality provided
hello_world_bp = Blueprint("hello_world", __name__)

# ~~~~~~ Hello world endpoints ~~~~~~
# define endpoint for request and list of HTTP methods request can have
@hello_world_bp.route("/hello_word", methods=["GET"])
def hello_world():
    # 200 OK code given by default
    response_body = "Hello, World!"
    return response_body

@hello_world_bp.route("/hello/JSON", methods=["GET"])
def hello_json():
    return {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"],
    }

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"],
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body