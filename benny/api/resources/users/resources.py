import falcon

class Index(object):
    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.body = ('Collection of users')

class ReadEmail(object):
    def on_get(self, request, response, email):
        response.status = falcon.HTTP_200
        response.body = ('User returned')

class ReadId(object):
    def on_get(self, request, response, id):
        response.status = falcon.HTTP_200
        response.body = ('User returned')

class Update(object):
    def on_put(self, request, response, id):
        response.status = falcon.HTTP_200
        response.body = ('Updated user')

class Delete(object):
    def on_delete(self, request, response, id):
        response.status = falcon.HTTP_200
        response.body = ('User deleted')