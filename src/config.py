import os


def get_database_connection_url():
    return os.getenv("DATABASE_URL")