from flask import Flask
from .extentions import db
from .routes.books import books


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'

    app.register_blueprint(books)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
