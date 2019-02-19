from sqlalchemy import create_engine, orm

# Class that holds the engine and current session
class Database:

    # TODO: connection string via config
    # Constructor with the connection string
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:piraatkat@127.0.0.1/benny')
        self.session = None

    # Create a new session
    def connect(self):
        sessionmaker = orm.sessionmaker(
            bind=self.engine,
            autoflush=True,
            autocommit=True,
            expire_on_commit=True
        )
        self.session = orm.scoped_session(sessionmaker)

    # Close the given session
    @staticmethod
    def close(session):
        session.flush()
        session.close()
        session.remove()

# Class that serves as a middleware database provider
class DatabaseMiddleWare:

    # Constructor which intializes the database class
    def __init__(self):
        self.database = Database()

    # Process the request after routing it
    def process_resource(self, request, response, resource, params):
        self.database.connect()
        resource.session = self.database.session

    # Post processing of the response after routing it
    def process_response(self, request, response, resource, params):
        if hasattr(resource, 'session'):
            self.database.close(resource.session)
