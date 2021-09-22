from flask import Flask
from flask_cors import CORS
from .config import config_by_name
from .api_rest import blueprint


def create_app() -> Flask:
    serve = Flask(__name__)
    serve.config.from_object(config_by_name['dev'])
    CORS(serve, origins="http://localhost",
         allow_headers=["Content-Type", "Authorization",
                        "Access-Control-Allow-Credentials"],
         supports_credentials=True)
    CORS(serve)
    serve.register_blueprint(blueprint)
    return serve


app = create_app()


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
