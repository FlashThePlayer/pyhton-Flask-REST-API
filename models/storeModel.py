from db import db
import json

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True)

    #somehow knows that this is a many to one relationship so its a freaking list 
    #fking sqlalchemy man, magic everywhere
    items = db.relationship('ItemModel', lazy = 'dynamic') 
    #lazy = 'dynamic' changes its behavior. items is no longer a loaded objects list but
    #a query builder which has to be called with .all() so it gets in the table and loads the objects
    #this save resources but also slower because we have to call the items everytime now

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=id)

    @classmethod
    def find_all_stores(cls):
        return {'stores': [cls.json(item) for item in cls.query.all()]}


    def save_store(self):
        db.session.add(self)
        db.session.commit()

    def delete_store(self):
        db.session.delete(self)
        db.session.commit()