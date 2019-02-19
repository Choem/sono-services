import falcon

class AuthResource(object):
    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.body = ('Auth endpoint.')