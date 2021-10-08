from .http import Http
import sympy as sym


class DerivativeController(Http):
    x, y, z = sym.symbols('x y z')

    # Derivada
    def derivate_expression(self, body):

        related_to = body['related_to']
        result = sym.diff(body['expression'], related_to)
        print(result)
        return self.ok({
            "result": str(result)
        })

    # Derivada sucessiva
    def successive_derivation(self, body):
        related_to = body['related_to']
        if related_to != 'x' or 'y' or 'z':
            return self.bad_request({
                "error": "Only x, y and z are supported"
            })
        result = sym.diff(body['expression'], related_to, body['times'])
        print(result)
        return self.ok({
            "result": str(result)
        })
