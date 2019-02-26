from api.config import Config

from falcon_auth import FalconAuthMiddleware, JWTAuthBackend

class Auth:
    def __init__(self, config):
        self.user_loader = lambda email, password: { 'email', email }
        self.auth_backend = JWTAuthBackend(
            self.user_loader, 
            algorithm='HS256',
            secret_key=config.rules['JWT_SECRET'], 
            auth_header_prefix=config.rules['JWT_HEADER_PREFIX']
        )
        self._auth_middleware = FalconAuthMiddleware(
            self.auth_backend,
            exempt_routes=['/auth/register', '/auth/login'],
            exempt_methods=None,
        )

    @property
    def auth_middleware(self):
        return self._auth_middleware

class AuthMiddleware:
    def __init__(self, config):
        self.auth = Auth(config)

    def process_resource(self, request, response, resource, params):
        self.auth.auth_middleware.process_resource(request, response, resource, params)