from db import db
import json

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {'name': self.username, 'price': self.password}

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id)

    @classmethod
    def find_all_users(cls):
        return {'users': [cls.json(user) for user in cls.query.all()]}


    def insert_user(self):
        db.session.add(self)
        db.session.commit()