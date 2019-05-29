import json
from flask_restful import Resource
from flask_restful import reqparse

from models.item import ItemModel

parser = reqparse.RequestParser()

class Items(Resource):
    def get(self):
       return ItemModel.find_all_items()


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This filed cannot be left blank!"
    )

    parser.add_argument('store_id',
        type=int,
        required=True,
        help="Every item needs a store_id!"
    )

    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            result = item.json(), 200
        else:
            result = None, 400
        return result

    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return {'message': 'Item {} already exists!'.format(name)}, 400
        else:
            data = Item.parser.parse_args()
            item = ItemModel(None, name, data['price'], data['store_id'])
            item.save_item()
            return item.json()

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if not item:
            return {'message': 'there is no such item!' }, 404 
        else:
            item.delete_item()
            return {'message': 'Item deleted sucessfull!'}, 200

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item:
            item.price = data['price']
            item.store_id = data['store_id']
        else:
            item = ItemModel(None ,name, data['price'], data['store_id'])
             
        item.save_item()
        return item.json()

        

        
