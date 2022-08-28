"""
    ToDo: DocString
"""
import uuid
from typing import Any
from pydantic import validator
from common.validators import DeferredValidator
from common.utils import Messages


class UpdatePersonCommand(DeferredValidator):
    """ ToDo: DocString """
    uid: str = None
    name: str = None
    last_name: str = None

    @classmethod
    def new(cls, request: Any):
        """ ToDo: DocString """
        body = request.json
        uid = body.get("uid", str(uuid.UUID(int = 0)))
        name = body.get("name")
        last_name = body.get("last_name")
        new_instance = cls.create_instance(uid = uid, name = name, last_name = last_name)

        return new_instance.validate()

    @validator("uid")
    def uid_must_be_valid(cls, value):
        """ ToDo: DocString """
        assert value != str(uuid.UUID(int = 0)), Messages.MUST_BE_VALID

        return value

    @validator("name")
    def name_must_have_more_than_2_chars(cls, value):
        """ ToDo: DocString """
        assert value is None or len(value) > 2, Messages.MORE_THAN_2_CHARS

        return value

    @validator("last_name")
    def last_name_must_have_more_than_2_chars(cls, value):
        """ ToDo: DocString """
        assert value is None or len(value) > 2, Messages.MORE_THAN_2_CHARS

        return value
