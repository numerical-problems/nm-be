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
            serie = fourier_series(expression, (x, int(first_interval), int(second_interval)))
            serie_result = serie.truncate(int(n))
            return self.__check_nan(serie_result)
        except Exception as e:
            return self.server_error(e)

    def __check_nan(self, serie_result):
        return (
            self.ok(dict(result="Invalid expression"))
            if serie_result == nan
            else self.ok(dict(result=str(serie_result)))
        )
