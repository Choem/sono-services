from .resources import Index, ReadId, ReadEmail, Update, Delete

routes = [
    ('/users', Index()),
    ('/users/read/id/{id:int}', ReadId()),
    ('/users/read/email/{email}', ReadEmail()),
    ('/users/update/{id:int}', Update()),
    ('/users/delete/{id:int}', Delete())
]