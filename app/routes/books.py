from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route('', methods=["POST"])
def create_new_book():
    request_body = request.get_json()
    if "title" not in request_body or "description" not in request_body:
        return make_response(
            "Invalid Request: Book title and description required",
            400
        )
    new_book = Book(
        title=request_body["title"],
        description=request_body["description"],
    )
    db.session.add(new_book)
    db.session.commit()
    return make_response(
        f"{new_book.title} Successfully Created", 201
    )

@books_bp.route('', methods=["GET"])
def read_all_books():
    # query all reports in db using Book instance
    books = Book.query.all()
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description,
        })
    return jsonify(books_response), 200
