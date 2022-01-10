import os

db_host = os.getenv("DB_HOST", "127.0.0.1")
db_password = os.getenv("DB_PASSWD", "123456")
db_user = os.getenv("DB_USER", "auth")
db_port = os.getenv("DB_PORT", "5432")
