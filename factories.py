from flask import Flask
from flask import jsonify
from users import usersBluePrint

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    app.register_blueprint(usersBluePrint)

    return app