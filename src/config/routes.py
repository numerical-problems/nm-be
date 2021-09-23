from flask_restx import Api
from src.routes.sum_routes import api as sum_api


def set_routes(api: Api) -> Api:
    # example
    #api.add_namespace(user_api, path='/users')
    api.add_namespace(sum_api, path='/sums')
    return api
