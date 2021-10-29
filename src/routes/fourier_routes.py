from flask_restx import Resource
from flask import request
from src.utils.dto import SerieFourierDto
from src.controllers.fourier_serie_controller import FourierSerieController


api = SerieFourierDto.api
_body_fourier = SerieFourierDto.body


@api.route('/', strict_slashes=False)
class Fourier(Resource, FourierSerieController):

    @api.expect(_body_fourier, validate=True)
    def post(self):
        return self.calculate(body=request.json)
