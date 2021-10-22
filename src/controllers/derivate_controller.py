from .http import Http
import sympy as sym
from sympy.abc import x, y, z
from sympy import Derivative


class DerivativeController(Http):

    # Derivada
    def derivate_expression(self, body):
        expr = body['expression']
        related_to = body['related_to']
        times = body['times'] if 'times' in body else 1
        if related_to == 'x' or related_to == 'y' or related_to == 'z':
            try:
                result = Derivative(expr)
                return self._return_result(result.doit())

            except Exception as e:
                return self.server_error()
        else:
            return self.bad_request({
                "error": "Only x, y and z are supported"
            })

    def _return_result(self, result):
        return self.ok({
            "result": str(result)
        })
