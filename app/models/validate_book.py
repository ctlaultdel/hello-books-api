from flask import abort, make_response
from .book import Book

def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        # abort raises HTTPException 
        # make_response returns a Flask response object to override html default return by abort
        abort(make_response({
            "message":f"book {book_id} invalid"}, 400
        ))
    book = Book.query.get(book_id)
    if not book:
        abort(make_response({
            "message": f"book {book_id} not found"}, 404
        ))
    return book
