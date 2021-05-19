from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST']) 
def login():
    data = request.form
    print(data)
    return render_template("login.html")


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        nickname = request.form.get('nickname')
        password = request.form.get('password')
        _password = request.form.get('password-confirm')

        if len(email) < 4:
            flash('Email Address is too short', category='error')
        elif len(nickname) < 2:
            flash('Your nickname is too short', category='error')
        elif password != _password:
            flash('Your passwords dont match', category='error')
        elif len(password < 8):
            flash('Your password is too short', category='error')
        else:
            flash('Sign Up Successful!', category='success')

    return render_template("signup.html")
