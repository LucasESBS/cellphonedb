from flask_restful import Api

from cellphonedb.api_endpoints.web_api.method_web_api_endpoints import method_web_api_routes


def add(api: Api, prefix=''):
    method_web_api_routes.add(api, prefix=prefix + '/method')