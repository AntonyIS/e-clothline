from app import db
from datetime import datetime
from flask_login import UserMixin
from app import login

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64), index=True)
    middlename = db.Column(db.String(64), index=True)
    lastname = db.Column(db.String(64), index=True)
    role = db.Column(db.String(64), index=True, default="user")
    phone = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    products = db.relationship('Products', backref='client', lazy='dynamic')


    def __repr__(self):
        return '<User {}>'.format(self.firstname) 



class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(140), index=True)
    size = db.Column(db.Integer)
    price = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    front_picture = db.Column(db.String(255), index=True)
    back_picture = db.Column(db.String(255), index=True)
    side_picture = db.Column(db.String(255), index=True)
   

    def __repr__(self):
        return '<Product {}>'.format(self.name)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))