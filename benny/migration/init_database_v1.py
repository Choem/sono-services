from playhouse.migrate import migrate
from migration.base_migration import BaseMigration


class InitDatabaseV1(BaseMigration):
    def migrate(self):
        migrate()

