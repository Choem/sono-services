from .resources import UsersResource, UserResource, FindByEmailResource

routes = [
    ('/users', UsersResource()),
    ('/users/{id:int}', UserResource()),
    ('/users/email/{email}',  FindByEmailResource())
]