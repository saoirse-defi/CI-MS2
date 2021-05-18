from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login') 
def login():
    return "<p>Logged in you cunt!</p>"
