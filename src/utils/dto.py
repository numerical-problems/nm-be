from flask_restx import Namespace, fields
from flask_cors import cross_origin

# Dto crie a namespace e declare  o corpo da requisição


class SumDto:
    api = Namespace('sum', description='operations of sum',
                    decorators=[cross_origin()])
    body = api.model('sum', {
        'sum1': fields.Integer(required=True),
        'sum2': fields.Integer(required=True)
    })
