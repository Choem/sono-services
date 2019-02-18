require('dotenv').config();

module.exports = {
    "type": process.env.DB_DRIVER,
    "host": process.env.DB_HOST,
    "port": process.env.DB_PORT,
    "username": process.env.DB_USERNAME,
    "password": process.env.DB_PASSWORD,
    "database": process.env.DB_NAME,
    "logging": process.env.DB_LOGGING,
    "entities": ['src/entities/**/**.entity.ts'],
    "migrations": ['src/migrations/**/**.ts'],
    "extra": {
      "charset": process.env.DB_CHARSET
    },
    "cli": {
        "migrationsDir": "src/migrations"
    }
};
