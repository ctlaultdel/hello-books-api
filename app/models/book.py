from app import db

# inherits db.Model from SQLAlchemy
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    # link Book model to table in postgres 'books' default=class_name
    __tablename__ = 'books'
