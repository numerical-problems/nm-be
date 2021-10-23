from flask_restx import Namespace, fields
from sympy.polys.fields import field

# Dto crie a namespace e declare  o corpo da requisição


class SumDto:
    api = Namespace('sum', description='operations of sum')
    body = api.model('sum', {
        'sum1': fields.Integer(required=True),
        'sum2': fields.Integer(required=True)
    })

class SerieFourierDto:
    api = Namespace('fourier')
    body = api.model('fourier', {
        'first_interval': fields.Integer(required=True),
        'second_interval': fields.Integer(required=True),
        'expression': fields.String(required=True),
        'n': fields.Integer(required=True)
    })

class derivationDto:
    api = Namespace('derivation', description='operation of derivation')
    body = api.model('derivation', {
        'expression': fields.String(require=True),
        'related_to': fields.String(required=True),
        'times': fields.Integer(required=False)
    })
