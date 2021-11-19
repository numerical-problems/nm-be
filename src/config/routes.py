from flask_restx import Api
from src.routes.sum_routes import api as sum_api
from src.routes.derivate_routes import api as derivate_api
from src.routes.fourier_routes import api as fourier_api
from src.routes.integrate_routes import api as integrate_api
from src.routes.interpolation_routes import api as interpolation_api
from src.routes.bissection_routes import api as bissection_api


def set_routes(api: Api) -> Api:
    # example
    # api.add_namespace(user_api, path='/users')
    api.add_namespace(sum_api, path="/sums")
    api.add_namespace(derivate_api, path="/derivate")
    api.add_namespace(fourier_api, path="/fourier")
    api.add_namespace(integrate_api, path="/integrals")
    api.add_namespace(interpolation_api, path="/interpolation")
    api.add_namespace(bissection_api,path='/bissection')
    return api
