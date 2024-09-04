import uuid
from datetime import datetime, tzinfo


class Utils:
    @staticmethod
    def str2bool(s: str) -> bool:
        return s.lower() in ['true', '1', 't', 'y', 'yes']

    @staticmethod
    def generate_uuid() -> str:
        return str(uuid.uuid4())

    @staticmethod
    def current_timestamp(time_zone: tzinfo = None) -> str:
        return datetime.now(tz=time_zone).isoformat()
