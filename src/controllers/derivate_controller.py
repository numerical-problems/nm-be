from .http import Http
import sympy as sym


class DerivativeController(Http):

    def derivate_expression(self, body):
        x, y, z = sym.symbols('x y z')
        related_to = body['related_to']
        result = sym.diff(body['expression'], related_to)
        print(result)
        return self.ok({
            "result": str(result)
        })
