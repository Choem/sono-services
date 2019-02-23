import falcon

class Register(object):
    def on_post(self, request, response):
        response.status = falcon.HTTP_200
        response.body = ('Registered user')

class Login(object):
    def on_post(self, request, response):
        response.status = falcon.HTTP_200
        response.body = ('Logged in user')