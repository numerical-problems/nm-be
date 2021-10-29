from flask_restx import Api
from flask import Blueprint
from .routes import set_routes

blueprint = Blueprint("api", __name__)


api = Api(
    blueprint,
    title="FLASK RESTPLUS(RESTX) API",
    version="1.0",
    description="a boilerplate for flask restplus (restx) web service",
)

api = set_routes(api)
