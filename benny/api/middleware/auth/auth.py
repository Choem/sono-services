import os

from falcon_auth import FalconAuthMiddleware, JWTAuthBackend

class Auth:
    def __init__(self):
        self.user_loader = lambda payload: payload['user']
        self._auth_backend = JWTAuthBackend(
            self.user_loader, 
            algorithm='HS256',
            secret_key=os.environ.get('JWT_SECRET'), 
            auth_header_prefix=os.environ.get('JWT_HEADER_PREFIX')
        )
        self._auth_middleware = FalconAuthMiddleware(
            self._auth_backend,
            exempt_routes=['/auth/register', '/auth/login'],
            exempt_methods=None
        )

    @property
    def auth_backend(self):
        return self._auth_backend

    @property
    def auth_middleware(self):
        return self._auth_middleware

class AuthMiddleware:
    def __init__(self):
        self.auth = Auth()

    def process_resource(self, request, response, resource, params):
        request.context['auth'] = self.auth.auth_backend
        self.auth.auth_middleware.process_resource(request, response, resource, params)