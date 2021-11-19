from flask_restx import Namespace, fields
from sympy.polys.fields import field

# Dto crie a namespace e declare  o corpo da requisição


class SumDto:
    api = Namespace("sum", description="operations of sum")
    body = api.model(
        "sum", {"sum1": fields.Integer(required=True), "sum2": fields.Integer(required=True)}
    )


class SerieFourierDto:
    api = Namespace("fourier")
    body = api.model(
        "fourier",
        {
            "first_interval": fields.Float(required=True),
            "second_interval": fields.Float(required=True),
            "expression": fields.String(required=True),
            "n": fields.Integer(required=True),
        },
    )


class derivationDto:
    api = Namespace("derivation", description="operation of derivation")
    body = api.model(
        "derivation",
        {
            "expression": fields.String(require=True),
            "related_to": fields.String(required=True),
            "times": fields.Integer(required=False),
        },
    )


class integralsDto:
    api = Namespace("integrals", description="operation of integrals")
    body = api.model(
        "integrals",
        {
            "expression": fields.String(require=True),
            "related_to": fields.String(required=True),
            "limits": fields.String(required=False),
            "superior_limit": fields.Integer(required=False),
            "inferior_limit": fields.Integer(required=False),
        },
    )

class interpolationDto:
    api = Namespace("interpolation", description="operation of polynomial interpolation")
    body = api.model(
        "interpolation",
        {
            "coordinates": fields.String(required=True)
        },
    )

class curveFitDto:
    api = Namespace("curveFit", description="operation of curve fit")
    body = api.model(
        "curveFit",
        {
            "pointsX": fields.String(required=True),
            "pointsY": fields.String(required=True),
        }
    )