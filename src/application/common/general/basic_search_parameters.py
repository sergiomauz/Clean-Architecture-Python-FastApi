"""
    ToDo: DocString
"""

from typing import Any
from common.validators import DeferredValidator


class BasicSearchParameters(DeferredValidator):
    """ ToDo: DocString """
    current_page: int
    page_size: int
    filter_value: str

    @classmethod
    def new(cls, request: Any = None):
        """ ToDo: DocString """
        current_page = request.args.get(key = "current_page", default = 1, type = int)
        page_size = request.args.get(key = "page_size", default = 25, type = int)
        filter_value = request.args.get(key = "filter_value", default = "", type = str)

        new_instance = cls.create_instance(current_page = current_page,
                                           page_size = page_size,
                                           filter_value = filter_value)

        return new_instance.validate()
