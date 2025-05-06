from app import db
from flask_login import UserMixin
from flask_login import LoginManager
from app import login
#login = LoginManager()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))
    email = db.Column(db.String(32))
    profile = db.relationship('UserCopy', backref = 'user', uselist = False, cascade = "all, delete")
    def __repr__(self):
        return '<User> ()>'.format(self.username)

def load_user(id):
    return User.query.get(int(id))
