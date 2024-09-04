import os


class Database:
    URL = os.environ.get('DATABASE_URL', 'sqlite:///database.db')
