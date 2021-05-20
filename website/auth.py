from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
            else:
                flash('Incorrect password, try again!', category='error')
        else:
            flash('Email is not recognised!', category='error')

    return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
    return "<h1>Logged out</h1>"


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        nickname = request.form.get('nickname')
        password = request.form.get('password')
        _password = request.form.get('password-confirm')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exists', category='error')
        elif len(email) < 4:
            flash('Email Address is too short', category='error')
        elif len(nickname) < 2:
            flash('Your nickname is too short', category='error')
        elif password != _password:
            flash('Your passwords dont match', category='error')
        elif len(password) < 8:
            flash('Your password is too short', category='error')
        else:
            new_user = User(
                email=email, 
                nickname=nickname, 
                password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Sign Up Successful!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", boolean=True)
