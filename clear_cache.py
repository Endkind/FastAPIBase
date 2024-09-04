import os

from logger import logger


def remove_python_caches(directory: str = "."):
    for root, dirs, files in os.walk(directory, topdown=False):
        if '__pycache__' in dirs:
            pycache_path = os.path.join(root, '__pycache__')
            try:
                for file in os.listdir(pycache_path):
                    if file.endswith('.pyc'):
                        file_path = os.path.join(pycache_path, file)
                        os.remove(file_path)
                        logger.debug(f"Deleting: {file_path}")

                os.rmdir(pycache_path)
                logger.debug(f"Deleted: {pycache_path}")
            except Exception as e:
                logger.error(f"Error while deleting {file_path}: {e}")

        for file in files:
            if file.endswith('.pyc'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    logger.debug(f"Deleted: {file_path}")
                except Exception as e:
                    logger.error(f"Error while deleting {file_path}: {e}")


if __name__ == "__main__":
    remove_python_caches()
