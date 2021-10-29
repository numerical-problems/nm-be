from flask_restx import Resource
from flask import request
from src.utils.dto import derivationDto, integralsDto
from src.controllers.integrals_controller import IntegralsController


api = integralsDto.api
_body_derivate = integralsDto.body


@api.route("/", strict_slashes=False)
class Integrate(Resource, IntegralsController):
    def post(self):
        return self.integrate_expression(body=request.json)


# @api.route("/successive", strict_slashes=False)
# class SuccesiveIntegration(Resource, IntegralsController):
#     def post(self):
#         return self.successive_derivation(body=request.json)
