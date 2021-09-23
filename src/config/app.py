from flask import Flask
from .config import config_by_name
from .api_rest import blueprint


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name['dev'])
    app.register_blueprint(blueprint)
    return app
