import datetime

from peewee import MySQLDatabase, Model, CharField, BooleanField, DateTimeField
from playhouse.migrate import MySQLMigrator

db = MySQLDatabase(
    'benny', 
    user='root', 
    password='piraatkat', 
    host='127.0.0.1', 
    port=3306
)

migrator = MySQLMigrator(db)

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    email = CharField(unique=True)
    password = CharField()
    name = CharField()
    is_activated = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.datetime.now)

def init_database():
    try:
        db.connect()
        # db.create_tables([User])
    except:
        raise Exception('Something did go wrong when initializing the database.')