from .http import Http
import numpy as np
from sympy import *

class InterpolationController(Http):
    def calculation(self, body):
      coordinates = body["coordinates"]
      return self._return_result(coordinates)

    # def interpolation_expression(self, body):
    #     try:
    #         expression = return calculation()
    #         return self._return_result(expression)
    #     except Exception as e:
    #         if str(e).find("Sympify of expression 'could not parse") != -1:
    #             return self.bad_request({"expressionError": "The expression is not valid"})
    #         return self.server_error()

    def _return_result(self, result):
        return self.ok({"result": str(result)})

    