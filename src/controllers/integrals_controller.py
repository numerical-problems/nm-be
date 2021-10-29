from .http import Http
import sympy as sym
from sympy import *


class IntegralsController(Http):
    def integrate_expression(self, body):
        try:
            expression = body["expression"]
            related_to = sym.symbols(body["related_to"])
            result = sym.integrate(expression, related_to)
            return self._return_result(result)
        except Exception as e:
            if str(e).find("Sympify of expression 'could not parse") != -1:
                return self.bad_request({"expressionError": "The expression is not valid"})
            return self.server_error()

    def integrate_with_limits(self, body):
        try:
            expression = body["expression"]
            related_to = sym.symbols(body["related_to"])
            superior_limit = body["superior_limit"]
            inferior_limit = body["inferior_limit"]
            result = sym.integrate(expression, (related_to, inferior_limit, superior_limit))
            return self._return_result(result)
        except Exception as e:
            if str(e).find("Sympify of expression 'could not parse") != -1:
                return self.bad_request({"expressionError": "The expression is not valid"})
            return self.server_error()

    def _return_result(self, result):
        return self.ok({"result": str(result)})
