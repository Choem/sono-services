import json
import falcon

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict

ERR_UNKNOWN = {
    'status': falcon.HTTP_500,
    'code': 500,
    'title': 'Unknown Error'
}

ERR_INVALID_PARAMETER = {
    'status': falcon.HTTP_400,
    'code': 400,
    'title': 'Invalid Parameter'
}

ERR_PASSWORD_NOT_MATCH = {
    'status': falcon.HTTP_400,
    'code': 400,
    'title': 'Password Not Match'
}

ERR_MISSING_DATA = {
    'status': falcon.HTTP_500,
    'code': 500,
    'title': 'Missing Data'
}

ERR_MISSING_DATABASE_SESSION = {
    'status': falcon.HTTP_500,
    'code': 500,
    'title': 'Missing Database Session'
}


class ApiError(Exception):
    def __init__(self, error=ERR_UNKNOWN, description=None):
        self.error = error
        self.error['description'] = description

    @property
    def code(self):
        return self.error['code']

    @property
    def title(self):
        return self.error['title']

    @property
    def status(self):
        return self.error['status']

    @property
    def description(self):
        return self.error['description']


class UnkownError(ApiError):
    def __init__(self, description=None):
        super().__init__(ERR_UNKNOWN)
        self.error['description'] = description


class InvalidParameterError(ApiError):
    def __init__(self, description=None):
        super().__init__(ERR_INVALID_PARAMETER)
        self.error['description'] = description


class PasswordNotMatchError(ApiError):
    def __init__(self, description=None):
        super().__init__(ERR_PASSWORD_NOT_MATCH)
        self.error['description'] = description


class MissingDataError(ApiError):
    def __init__(self, description=None):
        super().__init__(ERR_MISSING_DATA)
        self.error['description'] = description


class MissingDatabaseSessionError(ApiError):
    def __init__(self, description=None):
        super().__init__(ERR_MISSING_DATABASE_SESSION)
        self.error['description'] = description