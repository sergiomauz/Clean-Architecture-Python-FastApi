"""
    ToDo: DocString
"""
from typing import Any, List
from pydantic import validator
from common.validators import DeferredValidator
from common.utils import Messages, is_valid_array_of_uuids


class DeletePersonCommand(DeferredValidator):
    """ ToDo: DocString """
    uids: List[str]

    @classmethod
    def new(cls, request: Any):
        """ ToDo: DocString """
        body = request.json
        uids = body.get("uids")
        new_instance = cls.create_instance(uids = uids)

        return new_instance.validate()

    @validator("uids")
    def uuids_must_be_valids(cls, values):
        """ ToDo: DocString """
        assert is_valid_array_of_uuids(values), Messages.ALL_ITEMS_MUST_BE_VALIDS

        return values
