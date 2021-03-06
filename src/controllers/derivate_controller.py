from .http import Http
import sympy as sym
from sympy import *
import math


class DerivativeController(Http):
    x, y, z = sym.symbols("x y z")

    # Derivada
    def derivate_expression(self, body):
        if not body["related_to"] or int(body["related_to"].isnumeric()) == True:
            return self.bad_request("Verifique se todos os campos estão preenchidos corretamente")
        related_to = sym.symbols(body["related_to"])
        times = int(body["times"]) if "times" in body else 1
        try:
            result = sym.diff(body["expression"], related_to, times)
            return self._return_result(result)
        except Exception as e:
            if str(e).find("Sympify of expression 'could not parse") != -1:
                return self.bad_request("A expressão é inválida")
            return self.server_error()

    def _return_result(self, result):

        return self.ok(
            {"result": str(result).replace("**", "^").replace("*", "").replace("sqrt", "√")}
        )
