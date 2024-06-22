from flask import Flask
from .extentions import db
from .routes.books import books
from .routes.main import main


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'

    app.register_blueprint(books)
    app.register_blueprint(main)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
