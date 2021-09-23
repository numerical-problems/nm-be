from flask_restx import Resource
from flask import request

from src.utils.dto import SumDto
from src.controllers.sum_controller import SumController


api = SumDto.api
_body_sum = SumDto.body


@api.route('/', strict_slashes=False)
class Sum(Resource, SumController):

    @api.doc('Sum of a and b')
    # Valida o corpo da requisição de acordo com o que foi declarado na model em dto
    @api.expect(_body_sum, validate=True)
    def post(self):
        return self.sum_two_number(body=request.json)


@api.route('/<name>', strict_slashes=False)
class RouterWithParam(Resource):

    @api.doc('return your name')
    def get(self, name):
        return {'your_name': name}


@api.route('/query', strict_slashes=False)
class SumWithQuery(Resource, SumController):

    @api.doc('router with queries')
    def get(self):
        # Capturar queries da url
        value1 = request.args.get('value1')
        value2 = request.args.get('value2')
        return self.sum_two_number2(value1=value1, value2=value2)
