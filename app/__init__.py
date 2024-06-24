from flask import Flask
from .extentions import db
from .routes.main import main
from .routes.books import books
from .routes.about import about
from .routes.posts import posts
from .routes.user import user


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'

    app.register_blueprint(main)
    app.register_blueprint(books)
    app.register_blueprint(about)
    app.register_blueprint(posts)
    app.register_blueprint(user)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app
