import os


class FastAPIConfig:
    HOST: str = os.environ.get('HOST', '0.0.0.0')
    PORT: int = int(os.environ.get('PORT', 8000))