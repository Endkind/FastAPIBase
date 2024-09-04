import logging

from config import LoggerConfig

logging.basicConfig(
    level=LoggerConfig.LEVEL,
    format=LoggerConfig.FORMAT,
    datefmt=LoggerConfig.DATEFMT
)

logging.getLogger('apscheduler.executors.default').setLevel(LoggerConfig.LEVEL)

logger = logging.getLogger(__name__)
