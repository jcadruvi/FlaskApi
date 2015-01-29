from flask import Blueprint, jsonify, request
from flask.ext.restful import reqparse

bp = Blueprint('users', __name__)
usersBluePrint = Blueprint('users', __name__)

userList = {
    "users": [
        { "id": 1, "name": "John Doe" },
        { "id": 2, "name": "Jane Doe" },
        { "id": 3, "name": "John Smith" },
        { "id": 4, "name": "Jane Smith" }
    ]
}

@usersBluePrint.route('/api/users/get', methods=['GET'])
def get():
    parser = reqparse.RequestParser()
    parser.add.arguement('id', type=str, required=True, help="id is required.")
    args = parser.parse_args()
    for user in userList["users"]:
        if user["id"] == args.id:
            return jsonify(user)

@usersBluePrint.route('/api/users/get_all', methods=['GET'])
def get_all():
    return jsonify(userList)
