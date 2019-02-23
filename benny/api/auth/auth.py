from api.config import Config

from falcon_auth import FalconAuthMiddleware, JWTAuthBackend

class Auth:
    def __init__(self):
        self.user_loader = lambda email, password: { 'email', email }
        self.auth_backend = JWTAuthBackend(
            self.user_loader, 
            algorithm='HS256',
            secret_key=Config.JWT_SECRET, 
            auth_header_prefix='Bearer '
        )
        self._auth_middleware = FalconAuthMiddleware(
            self.auth_backend,
            exempt_routes=None,
            exempt_methods=['HEAD'],
        )

    @property
    def auth_middleware(self):
        return self.auth_middleware

class AuthMiddleware:
    def __init__(self):
        self.auth = Auth()

    def __repr__(self):
        return repr(self.auth.auth_middleware)

    def process_resource(self, request, response, resource, params):
        print('Process resource auth')

    def process_response(self, request, response, resource, params):
        print('Process response auth')