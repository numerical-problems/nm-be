from flask_restx import Namespace, fields

# Dto crie a namespace e declare  o corpo da requisição


class SumDto:
    api = Namespace('sum', description='operations of sum')
    body = api.model('sum', {
        'sum1': fields.Integer(required=True),
        'sum2': fields.Integer(required=True)
    })
