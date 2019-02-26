import falcon
import bcrypt

from cerberus import Validator
from cerberus.errors import ValidationError

from api.common.errors import InvalidParameterError, MissingDatabaseSessionError, MissingDataError, UnkownError, PasswordNotMatchError, UserNotExistsError
from api.resources.base import BaseResource
from api.models import User


REGISTER_FIELDS = {
    'username': {
        'type': 'string',
        'required': True,
        'minlength': 5,
        'maxlength': 255
    },
    'email': {
        'type': 'string',
        'regex': '[a-zA-Z0-9._-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,4}',
        'required': True
    },
    'password': {
        'type': 'string',
        'required': True,
        'minlength': 6
    },
    'password_confirm': {
        'type': 'string',
        'required': True,
        'minlength': 6
    }
}


def validate_register_fields(request, response, resource, params):
    schema = {
        'username': REGISTER_FIELDS['username'],
        'email': REGISTER_FIELDS['email'],
        'password': REGISTER_FIELDS['password'],
        'password_confirm': REGISTER_FIELDS['password_confirm']
    }

    validator = Validator(schema)
    
    try:
        if not validator.validate(request.context['data']):
            raise InvalidParameterError(validator.errors)
    except Exception:
        raise InvalidParameterError('Invalid Request {0}'.format(request.context))


class Register(BaseResource):
    @falcon.before(validate_register_fields)
    def on_post(self, request, response):
        session = request.context['session']
        data = request.context['data']

        if session and data:
            if data['password'] == data['password_confirm']:
                user = User()
                user.username = data['username']
                user.email = data['email']
                user.password = bcrypt.hashpw(data['password'].encode('utf8'), bcrypt.gensalt())

                session.add(user)
                session.commit()
            else:
                raise PasswordNotMatchError('Passwords do not match')
        elif not session:
            raise MissingDatabaseSessionError('Missing database session {0}'.format(request.context))
        elif not data:
            raise MissingDataError('Missing data {0}'.format(request.context))
        else:
            raise UnkownError('Something went wrong')

        self.on_success(response, 'User successfully registered')


LOGIN_FIELDS = {
    'email': {
        'type': 'string',
        'regex': '[a-zA-Z0-9._-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,4}',
        'required': True
    },
    'password': {
        'type': 'string',
        'required': True,
        'minlength': 6
    }
}


def validate_login_fields(request, response, resource, params):
    schema = {
        'email': REGISTER_FIELDS['email'],
        'password': REGISTER_FIELDS['password']
    }

    validator = Validator(schema)

    try:
        if not validator.validate(request.context['data']):
            raise InvalidParameterError(validator.errors)
    except Exception:
        raise InvalidParameterError('Invalid Request {0}'.format(request.context))


class Login(BaseResource):
    @falcon.before(validate_login_fields)
    def on_post(self, request, response):
        session = request.context['session']
        data = request.context['data']
        auth = request.context['auth']

        jwt = None
        
        if session and data and auth:
            email = data['email']
            password = data['password'].encode('utf8')
            
            user = session.query(User).filter_by(email=email).one_or_none()
            user.password = user.password.encode('utf8')
            
            if user:
                if bcrypt.checkpw(password, user.password):
                    jwt = auth.get_auth_token({ 'id': user.id })

                else:
                    raise PasswordNotMatchError('Passwords do not match')
            else:
                raise UserNotExistsError('User does not exists with email {0}'.format(email))

        elif not session:
            raise MissingDatabaseSessionError('Missing database session {0}'.format(request.context))
        elif not data:
            raise MissingDataError('Missing data {0}'.format(request.context))
        else:
            raise UnkownError('Something went wrong')

        self.on_success(response, 'User successfully logged in', { 'jwt': jwt })