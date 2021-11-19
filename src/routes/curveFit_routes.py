from flask_restx import Resource
from flask import request
from src.utils.dto import curveFitDto
from src.controllers.curveFit_controller import CurveFitController

api = curveFitDto.api
_body_curveFit = curveFitDto.body

@api.route("/", strict_slashes=False)
class CurveFit(Resource, CurveFitController):
    @api.expect(_body_curveFit, validate=True)
    def post(self):
        return self.curveFit_newPairs(body=request.json)