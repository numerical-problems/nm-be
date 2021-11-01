from .http import Http
import numpy as np
from sympy import *

class InterpolationController(Http):
    def stringToArray(self, string): #ex: 1,2;3,4 -> [[1.0, 2.0], [3.0, 4.0]]
      string = string.split(";")
      array = []
      aux = []
      for i in string:
        coordenada = i.split(",") 
        aux = []
        for j in coordenada:
          aux.append(float(j))
        array.append(aux)
      return array      

    def interpolation_expression(self, body):
        try:
            coordinates = body["coordinates"]
            array = self.stringToArray(coordinates) 
            return self._return_result(array) 
        except Exception as e:
            if str(e).find("Sympify of expression 'could not parse") != -1:
                return self.bad_request({"expressionError": "The expression is not valid"})
            return self.server_error()

    def _return_result(self, result):
        return self.ok({"result": str(result)})

    