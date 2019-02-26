import falcon

class Users(object):
    auth = {
        'auth_disabled': True
    }

    def on_get(self, request, response):
        session = request.context['session']

        users = session.query(User).all()

        response.status = falcon.HTTP_200
        response.body = users

class User(object):
    def on_get(self, request, response, id):
        response.status = falcon.HTTP_200
        response.body = ('User returned')

    def on_put(self, request, response, id):
        response.status = falcon.HTTP_200
        response.body = ('Updated user')

    def on_delete(self, request, response, id):
        response.status = falcon.HTTP_200
        response.body = ('User deleted')

class FindByEmail(object):
    def on_get(self, request, response, email):
        response.status = falcon.HTTP_200
        response.body = ('User returned')