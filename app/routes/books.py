from flask import Blueprint
from ..extentions import db
from ..models.books import Books

books = Blueprint('books', __name__)


@books.route('/books/<title>')
def create_books(title):
    book = Books(title=title)
    db.session.add(book)
    db.session.commit()
    return "Add a book!"
