import time
import grpc

import benny_service.benny_service_pb2 as benny_service_pb2
import benny_service.benny_service_pb2_grpc as benny_service_pb2_grpc

from concurrent import futures

from api.models import User

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def get_user_by_id(database, id):
    database.connect()
    user = database.session.query(User).filter_by(id=id).one_or_none() 
    database.close(database.session)
    return user 

def get_user_by_email(database, email):
    database.connect()
    user = database.session.query(User).filter_by(email=email).one_or_none() 
    database.close(database.session)
    return user

def get_paginated_users(database, request):
    database.connect()
    users = database.session.query(User).filter_by(id=request['id']).one_or_none() 
    database.close(database.session)
    return users

class AccountServiceServer(benny_service_pb2_grpc.AccountServiceServicer):
    def __init__(self, database):
        self.database = database
    
    def ReadUserById(self, request, context):
        user = get_user_by_id(self.database, request.id)
        if user is None:
            return benny_service_pb2.UserResponse()
        return benny_service_pb2.UserResponse(id=user.id, username=user.username, email=user.email)

    def ReadUserByEmail(self, request, context):
        user = get_user_by_email(self.database, request)
        if user is None:
            return benny_service_pb2.UserResponse()

        return user

    def Paginate(self, request, context):
        users = get_paginated_users(self.database, request)
        if users is None or len(users) == 0:
            return benny_service_pb2.PaginateResponse()

        return users


def serve(database):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    benny_service_pb2_grpc.add_AccountServiceServicer_to_server(AccountServiceServer(database), server)
    server.add_insecure_port('0.0.0.0:13373')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)