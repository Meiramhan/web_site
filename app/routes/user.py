from flask import Blueprint, render_template, request, redirect
from ..extentions import db
from ..models.users import Users
from werkzeug.security import generate_password_hash, check_password_hash


user = Blueprint('user', __name__)


@user.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        login = request.form['login']
        password = request.form['password']
        hash = generate_password_hash(password)
        confirm_password = request.form['confirm_password']

        post = Users(name=name, login=login, password=hash)

        if password == confirm_password:
            try:
                db.session.add(post)
                db.session.commit()
                return redirect('/')
            except:
                return 'Fail'

    else:
        return render_template('user/register.html')