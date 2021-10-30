from flask_restx import Resource
from flask import request
from src.utils.dto import interpolationDto
from src.controllers.interpolation_controller import InterpolationController

api = interpolationDto.api
_body_derivate = interpolationDto.body

@api.route("/", strict_slashes=False)
class Interpolation(Resource, InterpolationController):
    def post(self):
        return self.interpolation_expression(body=request.json)

