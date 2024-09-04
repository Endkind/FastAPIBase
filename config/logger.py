import os


class Logger:
    LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
    FORMAT = "%(asctime)-15s - %(levelname)s - %(message)s"
    DATEFMT = "[%X]"
