from flask_restx import Api


def set_routes(api: Api) -> Api:
    # example
    #api.add_namespace(user_api, path='/users')

    return api
