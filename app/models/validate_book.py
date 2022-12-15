from flask import abort, make_response
from .book import books

def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        # abort raises HTTPException 
        # make_response returns a Flask response object to override html default return by abort
        abort(make_response({"message":f"book {book_id} invalid"}, 400))
    for book in books:
        if book.id == book_id:
            return book
    abort(make_response({"message":f"book {book_id} not found"}, 404))