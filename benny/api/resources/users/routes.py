from .resources import Users, User, FindByEmail

routes = [
    ('/users', Users()),
    ('/users/{id:int}', User()),
    ('/users/email/{email}',  FindByEmail())
]