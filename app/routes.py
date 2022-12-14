# Blueprint groups related routes (endpoints)
from flask import Blueprint, jsonify

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


# ~~~~~~ Book Class ~~~~~~
class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Lollipops in the Rain", "A kids book about eating lollipops in the rain"),
    Book(2, "Dragons at sunrise", "A fantasy book about a child with a dragon friend"),
    Book(3, "Mai Tai Anytime", "An adult fiction book about a man who loves drinking Mai Tai's")
    ]


# url_prefix routes this blueprint to all routes that start with /books
books_bp = Blueprint("books", __name__, url_prefix="/books")

# ~~~~~~ books endpoint ~~~~~~
@books_bp.route("", methods=["GET"])
def handle_books():
    # initialize list
    books_response = []
    # format book attributes for each book
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    # return converted json
    return jsonify(books_response)
