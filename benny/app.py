import falcon

from resource.user_resource import UserResource
from resource.auth_resource import AuthResource

from models import init_database

# Intialize falcon API
api = application = falcon.API()

# Define authentication endpoint and resource
auth_resource = AuthResource()
api.add_route('/auth', auth_resource)

# Define users endpoint and resource 
user_resource = UserResource()
api.add_route('/users', user_resource)

# Initialize database
init_database()