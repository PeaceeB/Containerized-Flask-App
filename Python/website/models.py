from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class User(db.Model, UserMixin): # A model is basically a table
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # unique=True ensures that we do not have multiple users using the same email address. All email addresses must be unique
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now()) # We want to know the timezone of the time since it's date and time. And default=True when this section hasn't be filled, this fills this section in with whatever the current time is by default
    posts = db.relationship('Post', backref='user', passive_deletes=True)

    # __table_args__ = {'schema':'userschema'}


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now()) # We want to know the timezone of the time since it's date and time. And default=True when this section hasn't be filled, this fills this section in with whatever the current time is by default
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False) # Makes sure that if the author gets deleted, all of the posts will be deleted with the user
    # __table_args__ = {'schema':'postschema'}
