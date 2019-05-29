import os

from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api
from flask_restful import reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate
from security import identity

from resources.user import UserRegister
from resources.user import Users
from resources.item import Item
from resources.item import Items
from resources.store import Store
from resources.store import Stores

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'test'
api = Api(app)


jwt = JWT(app, authenticate, identity) #/auth


#api.add_resource macht die resource Student nutzbar spart den decorator 
api.add_resource(Item, '/item/<string:name>') #http://localhost:5000/item/rolf
api.add_resource(Items, '/items/')
api.add_resource(Users, '/users/')
api.add_resource(UserRegister, '/register/')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Stores, '/stores/')

if __name__ == '__main__':
    from db import db 
    db.init_app(app)
    app.run(port=5000, debug = True)