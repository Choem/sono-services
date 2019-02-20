import os
import falcon

from api.database import DatabaseMiddleware
from api.auth import AuthMiddleware
from api.router import Router
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
        users_routes
    ], api)

    return api

# Api holds the initialized falcon API
api = init_api()