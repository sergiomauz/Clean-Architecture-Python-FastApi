"""
    ToDo: DocString
"""
import uuid
import datetime
from typing import Any


def str_yyyymmdd_t(input_datetime: datetime) -> str:
    """ ToDo: DocString """
    return input_datetime.strftime("%Y-%m-%d %H:%M:%S") if input_datetime is not None else None


def convert_to_uuid(value : Any) -> uuid:
    """ ToDo: DocString """
    try:
        return uuid.UUID(str(value))
    except ValueError:
        return None


def is_valid_array_of_uuids(values : Any) -> bool:
    """ ToDo: DocString """
    try:
        list(map(lambda item: uuid.UUID(str(item)), values))
        return True
    except ValueError:
        return False
