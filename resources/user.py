import json
from flask_restful import Resource
from flask_restful import reqparse

from models.user import UserModel

parser = reqparse.RequestParser()
        

class Users(Resource):
    def get(self):
        return UserModel.find_all_users()
        # return json.dumps(result), 200
    

class UserRegister(Resource):
    parser.add_argument('username',
    type=str,
    required=True,
    help="This filed cannot be left blank!"
    )

    parser.add_argument('password',
    type=str,
    required=True,
    help="This filed cannot be left blank!"
    )

    def post(self):
        data = parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"Message" : "Username is already taken!"}, 400

        user = UserModel(**data)

        UserModel.insert_user(user)
        return {"Message" : "User created successfully"}, 201

