from .http import Http


class SumController(Http):
    def sum_two_number(self, body):
        total = sum([int(body["sum1"]), int(body["sum2"])])
        return self.ok(dict(total=total))

    # parametros opcionais
    def sum_two_number2(self, value1=None, value2=None):
        if not value1 or not value2:
            return self.bad_request()
        total = sum([int(value1), int(value2)])
        return self.ok(dict(total=total))
