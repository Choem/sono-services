import os
import falcon
import concurrent.futures
import logging

from alembic import command
from alembic.config import Config as AlembicConfig

from api.config import Config  as APIConfig
from api.router import Router

from api.middleware.database import DatabaseMiddleware, Database
from api.middleware.auth import AuthMiddleware, Auth
from api.middleware.translator import TranslatorMiddleware

from api.resources.auth.routes import routes as auth_routes
from api.resources.users.routes import routes as users_routes

from benny_service.benny_service_server import AccountServiceServer, serve as ServeGRPC

# Method for intializing the application
def init_api():
    # Connect to db and run migrations if needed
    alembic_config = AlembicConfig('alembic.ini')
    alembic_config.set_main_option('script_location', 'migrations')
    alembic_config.set_main_option('sqlalchemy.url', 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(
            os.environ.get('DB_USER_NAME'), 
            os.environ.get('DB_USER_PASSWORD'), 
            os.environ.get('DB_HOST'),
            os.environ.get('DB_NAME')
    ))
    command.upgrade(alembic_config, 'head')

    # Create a falcon API with our own middlewares
    api = falcon.API(middleware=[
        AuthMiddleware(),
        TranslatorMiddleware(),
        DatabaseMiddleware()
    ])

    # Register routes from the resources we have
    Router.register_routes([
        auth_routes,
        users_routes
    ], api)

    return api


def init_grpc():
    logging.info('Starting gRPC server...')
    ServeGRPC(Database())
    logging.info('Booted gRPC server!')

# Initialize API config
APIConfig()

# Execute API and gRPC in two different threads
executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
api = executor.submit(init_api).result()
executor.submit(init_grpc)
