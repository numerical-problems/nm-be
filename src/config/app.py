from flask import Flask
from flask_cors import CORS
from .config import config_by_name
from .api_rest import blueprint



def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(config_by_name['dev'])
    app.register_blueprint(blueprint)
    return app
