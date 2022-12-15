# Blueprint groups related routes (endpoints)
from flask import Blueprint, jsonify
from app.models.book import books
from app.models.validate_book import validate_book

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

@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    book = validate_book(book_id)
    # jsonify returns an http response object
    # don't need it here though b/c flask automatically converts dicts into HTTP response bodies
    # do you need it then if you are returning a list or something
    return {
        "id": book.id,
        "title": book.title,
        "description": book.description,
        }
