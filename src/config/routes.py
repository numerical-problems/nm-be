from flask_restx import Api
from src.routes.sum_routes import api as sum_api
from src.routes.derivate_routes import api as derivate_api
from src.routes.fourier_routes import api as fourier_api

def set_routes(api: Api) -> Api:
    # example
    #api.add_namespace(user_api, path='/users')
    api.add_namespace(sum_api, path='/sums')
    api.add_namespace(derivate_api,path='/derivate')
    api.add_namespace(fourier_api, path='/fourier')
    return api
