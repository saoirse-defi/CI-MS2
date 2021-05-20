from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    # each table needs a primary key
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # a foriegn key is needed when there is a many to one relationship
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    # each table needs a primary key
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    nickname = db.Column(db.String(100))
    # if a foriegn key is used then a relationship
    # must be made in the referenced table
    notes = db.relationship('Note')
