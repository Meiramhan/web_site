from flask import Blueprint, render_template
from ..models.books import Books

posts = Blueprint('posts', __name__)


@posts.route('/review', methods=['POST', 'GET'])
def review():
    data = Books.query.all()
    return render_template('/review/review.html', data=data)