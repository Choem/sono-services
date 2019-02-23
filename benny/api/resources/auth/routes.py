from .resources import Register, Login

routes = [
    ('/auth/register', Register()),
    ('/auth/login', Login())
]