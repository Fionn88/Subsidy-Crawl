import pymysql
import config

global conn

db_settings = {
    "host": config.DB_HOST,
    "port": int(config.DB_PORT),
    "user": config.DB_USER,
    "password": config.DB_PASSWORD,
    "db": config.DB_SCHEMA,
    "charset": "utf8"
}

conn = pymysql.connect(**db_settings)
