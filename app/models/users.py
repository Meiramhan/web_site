from ..extentions import db
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    login = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)