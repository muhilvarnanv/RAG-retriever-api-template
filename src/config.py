import os


def get_database_connection_url():
    return os.getenv("DATABASE_URL")


def get_collection_name():
    return os.getenv("COLLECTION_NAME")
