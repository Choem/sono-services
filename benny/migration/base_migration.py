from playhouse.migrate import MySQLMigrator

class BaseMigration:
    def __init__(self, database):
        self.migrator = MySQLMigrator(database)