import os
import falcon

# kanker
from falcon_auth import FalconAuthMiddleware, JWTAuthBackend
from api.config import Config 

from api.database import DatabaseMiddleware
from api.auth import AuthMiddleware, Auth
from api.router import Router

from api.resources.auth.routes import routes as auth_routes
from api.resources.users.routes import routes as users_routes 

# Method for intializing the application
def init_api():

    # Create a falcon API with our own database middleware
    api = falcon.API(middleware=[
        AuthMiddleware(),
        DatabaseMiddleware()
    ])

    # Register routes from the resources we have
    Router.register_routes([
        auth_routes,
        users_routes
    ], api)

    return api

# Api holds the initialized falcon API
api = init_api()