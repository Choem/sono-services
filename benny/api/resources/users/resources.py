import falcon

from api.models import User
from api.resources.base import BaseResource

class UsersResource(BaseResource):
    auth = {
        'auth_disabled': True
    }

    def on_get(self, request, response):
        session = request.context['session']

        users = [user.as_dict() for user in session.query(User).all()]

        self.on_success(response, 'Users returned', { 'users': users })


class UserResource(BaseResource):
    auth = {
        'auth_disabled': True
    }
    
    def on_get(self, request, response, id):
        session = request.context['session']

        user = session.query(User).filter_by(id=id).one_or_none()

        if not user:
            self.on_error(response, { 'message': 'User not found', 'code': 400, 'status': 'Bad Request' })
        else:
            self.on_success(response, 'User returned', user.as_dict())

    def on_put(self, request, response, id):
        response.status = falcon.HTTP_200
        response.body = ('Updated user')

    def on_delete(self, request, response, id):
        response.status = falcon.HTTP_200
        response.body = ('User deleted')


class FindByEmailResource(BaseResource):
    auth = {
        'auth_disabled': True
    }

    def on_get(self, request, response, email):
        session = request.context['session']

        user = session.query(User).filter_by(email=email).one_or_none()

        if not user:
            self.on_error(response, { 'message': 'User not found', 'code': 400, 'status': 'Bad Request' })
        else:
            self.on_success(response, 'User returned', user.as_dict())