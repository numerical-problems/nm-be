# Retornos Http

class Http():

    def no_content(self):
        return '', 204

    def ok(self, data):
        return data, 200

    def bad_request(self, message='Invalid Request'):
        return dict(message=message), 400
