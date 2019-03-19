from .resources import RegisterResource, LoginResource

routes = [
    ('/auth/register', RegisterResource()),
    ('/auth/login', LoginResource())
]