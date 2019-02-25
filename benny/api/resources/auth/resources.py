import falcon
import bcrypt

from cerberus import Validator
from cerberus.errors import ValidationError

from api.common.errors import InvalidParameterError, MissingDatabaseSessionError, MissingDataError, UnkownError, PasswordNotMatchError
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
    'pasword_confirm': {
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
        raise InvalidParameterError('Invalid Request %s' % request.context)


class Register(BaseResource):
    @falcon.before(validate_register_fields)
    def on_post(self, request, response):
        session = request.context['session']
        data = request.context['data']

        if session and data:
            if data['password'] is data['password_confirm']:
                user = User()
                user.username = data['username']
                user.email = data['email']
                user.password = bcrypt.hashpw(data['password'], bcrypt.gensalt())

                session.add(user)
                session.commit()
            else:
                raise PasswordNotMatchError('Passwords do not match')
        elif not session:
            raise MissingDatabaseSessionError('Missing database session %s' % request.context)
        elif not data:
            raise MissingDataError('Missing data %s' % request.context)
        else:
            raise UnkownError('Something went wrong')

        self.on_success(response, None)


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
        raise InvalidParameterError('Invalid Request %s' % request.context)


class Login(BaseResource):
    @falcon.before(validate_login_fields)
    def on_post(self, request, response):
        session = request.context['session']
        data = request.context['data']

        if session and data:
            # TODO: Authenticate via middleware stuff
            print(data)
        elif not session:
            raise MissingDatabaseSessionError('Missing database session %s' % request.context)
        elif not data:
            raise MissingDataError('Missing data %s' % request.context)
        else:
            raise UnkownError('Something went wrong')

        self.on_success(response, None)