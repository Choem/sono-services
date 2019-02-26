import os
import falcon

from api.config import Config 
from api.router import Router

from api.middleware.database import DatabaseMiddleware
from api.middleware.auth import AuthMiddleware, Auth
from api.middleware.translator import TranslatorMiddleware

from api.resources.auth.routes import routes as auth_routes
from api.resources.users.routes import routes as users_routes 

# Method for intializing the application
def init_api(config):

    # Create a falcon API with our own middlewares
    api = falcon.API(middleware=[
        AuthMiddleware(config),
        TranslatorMiddleware(),
        DatabaseMiddleware(config)
    ])

    # Register routes from the resources we have
    Router.register_routes([
        auth_routes,
        users_routes
    ], api)

    return api

# Config which holds the env file as key value pairs in rules dict
config = Config()

# Api holds the initialized falcon API
api = init_api(config)