import json
from flask_restful import Resource
from flask_restful import reqparse

from models.storeModel import StoreModel

class Stores(Resource):
    def get(self):
        return StoreModel.find_all_stores()

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        else:
            return None, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'Item {} already exists!'.format(name)}, 400
        else:
            store = StoreModel(name)
            store.save_store()
            return store.json()

    def put(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.name = name
        else:
            store = StoreModel(name)
        store.save_store()
        return store.json()

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        
        if store:
            store.delete_store()
            return {'message': 'Store was deleted!'}, 200
        else:
            return {'message': 'there is no such item!' }, 404 


        
