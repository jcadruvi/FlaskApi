from flask import Blueprint, jsonify, request


bp = Blueprint('users', __name__)
usersBluePrint = Blueprint('users', __name__)

@usersBluePrint.route('/api/users/get_all', methods=['GET'])
def users():
    userList = {
        "users": [
            { "id": 1, "name": "John Doe" },
            { "id": 2, "name": "Jane Doe" },
            { "id": 3, "name": "John Smith" },
            { "id": 4, "name": "John Smith" }
        ]}
    return jsonify(userList)
