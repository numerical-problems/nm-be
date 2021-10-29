from .http import Http
import sympy as sym
from sympy import *


class DerivativeController(Http):
    x, y, z = sym.symbols("x y z")

    # Derivada
    def derivate_expression(self, body):
        related_to = body["related_to"]
        times = int(body["times"]) if "times" in body else 1
        if related_to == "x" or related_to == "y" or related_to == "z":
            try:
                result = sym.diff(body["expression"], related_to, times)
                return self._return_result(result)
            except Exception as e:
                if str(e).find("Sympify of expression 'could not parse") != -1:
                    return self.bad_request({"expressionError": "The expression is not valid"})
                return self.server_error()
        else:
            return self.bad_request({"error": "Only x, y and z are supported"})

    def _return_result(self, result):
        return self.ok({"result": str(result)})
