import falcon

from cerberus import Validator
from cerberus.errors import ValidationError

from api.models import User
from api.resources.base import BaseResource
from api.common.errors import InvalidParameterError

class UsersResource(BaseResource):
    def on_get(self, request, response):
        session = request.context['session']
        # Get authenticated user (which only holds id)
        # authenticated_user = request.context['user']

        users = [user.as_dict() for user in session.query(User).all()]
        for user in users:
            del user['password']

        self.on_success(response, 'Users returned', { 'users': users })


UPDATE_FIELDS = {
    'username': {
        'type': 'string',
        'required': True,
        'minlength': 5,
        'maxlength': 255
    }
}

def validate_update_fields(request, response, resource, params):
    schema = {
        'username': UPDATE_FIELDS['username']
    }

    validator = Validator(schema)
    
    try:
        if not validator.validate(request.context['data']):
            raise InvalidParameterError(validator.errors)
    except Exception:
        raise InvalidParameterError('Invalid Request {0}'.format(request.context))


class UserResource(BaseResource):
    def on_get(self, request, response, id):
        session = request.context['session']

        user = session.query(User).filter_by(id=id).one_or_none()
        del user['password']

        if not user:
            self.on_error(response, { 'message': 'User not found', 'code': 400, 'status': 'Bad Request' })
        else:
            self.on_success(response, 'User returned', { 'id': user.id, 'username': user.username, 'email': user.email })

    @falcon.before(validate_update_fields)
    def on_put(self, request, response, id):
        session = request.context['session']
        data = request.context['data']

        try:
            session.query(User).filter(User.id == id).update({User.username: data['username']})
            session.commit()
            
            self.on_success(response, 'User updated')
        except:
            self.on_error(response, { 'message': 'User not found', 'code': 400, 'status': 'Bad Request' })

    def on_delete(self, request, response, id):
        session = request.context['session']

        try:
            session.query(User).filter(User.id == id).delete()
            session.commit()
            
            self.on_success(response, 'User deleted')
        except:
            self.on_error(response, { 'message': 'User not found', 'code': 400, 'status': 'Bad Request' })


class FindByEmailResource(BaseResource):
    def on_get(self, request, response, email):
        print(email)
        session = request.context['session']

        user = session.query(User).filter_by(email=email).one_or_none()

        if not user:
            self.on_error(response, { 'message': 'User not found', 'code': 400, 'status': 'Bad Request' })
        else:
            self.on_success(response, 'User returned', { 'id': user.id, 'username': user.username, 'email': user.email })