from flask_restx import Resource
from flask import request
from src.utils.dto import  integralsDto
from src.controllers.integrals_controller import IntegralsController


api = integralsDto.api


@api.route("/", strict_slashes=False)
class Integrate(Resource, IntegralsController):
    def post(self):
        return self.integrate_expression(body=request.json)


@api.route("/limits", strict_slashes=False)
class IntegrationWithLimit(Resource, IntegralsController):
    def post(self):
        return self.integrate_with_limits(body=request.json)
