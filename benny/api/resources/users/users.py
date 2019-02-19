import falcon

class Users(object):
    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.body = ('Collection of users')

    def on_post(self, request, response):
        response.status = falcon.HTTP_200
        response.body = ('Created a new user')