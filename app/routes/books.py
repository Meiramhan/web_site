from flask import Blueprint, render_template, request, redirect
from ..extentions import db
from ..models.books import Books

books = Blueprint('books', __name__)


@books.route('/post/adding', methods=['POST', 'GET'])
def adding():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']

        adding = Books(title=title, price=price)

        try:
            db.session.add(adding)
            db.session.commit()
            return redirect('/')
        except:
            return 'Fail'

    else:
        return render_template('post/adding.html')
