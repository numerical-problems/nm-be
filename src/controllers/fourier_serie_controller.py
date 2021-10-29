from .http import Http
from sympy import fourier_series
from sympy.core.numbers import nan
from sympy.abc import x


class FourierSerieController(Http):
    def calculate(self, body):
        try:
            expression = body["expression"]
            n = body["n"]
            first_interval = body["first_interval"]
            second_interval = body["second_interval"]
            if not "x" in expression:
                return self.bad_request(message='Missing "x" in expression')
            if float(first_interval) == float(second_interval):
                return self.bad_request(message="Intervals cannot be equal")
            serie = fourier_series(expression, (x, float(first_interval), float(second_interval)))
            serie_result = serie.truncate(int(n))
            return self.ok(dict(result=str(serie_result)))
        except Exception as e:
            return self.server_error(e)
