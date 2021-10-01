from flask_restx import Resource
from flask import request
from src.utils.dto import derivationDto
from src.controllers.derivate_controller import DerivativeController


api = derivationDto.api
_body_derivate = derivationDto.body


@api.route('/', strict_slashes=False)
class Derivate(Resource, DerivativeController):
    def post(self):
        return self.derivate_expression(body=request.json)
