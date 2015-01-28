from flask import Flask
from flask import jsonify


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    @app.route('/api/users', methods=['GET'])
    def users():
        userList = {
            "users": [
                { "id": 1, "name": "John Doe" },
                { "id": 2, "name": "Jane Doe" },
                { "id": 3, "name": "John Smith" },
                { "id": 4, "name": "John Smith" }
            ]}
        return jsonify(userList)


    return app