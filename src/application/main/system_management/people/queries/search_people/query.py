"""
    ToDo: DocString
"""

from typing import Any
from pydantic import validator
from common.validators import DeferredValidator
from application.common.general import BasicSearchParameters


class SearchPeopleQuery(BasicSearchParameters, DeferredValidator):
    """ ToDo: DocString """

    @classmethod
    def new(cls, request: Any = None):
        """ ToDo: DocString """
        basic_search_parameters = BasicSearchParameters.new(request)
        new_instance = cls.create_instance(current_page = basic_search_parameters.current_page,
                                           page_size = basic_search_parameters.page_size,
                                           filter_value = basic_search_parameters.filter_value)

        return new_instance.validate()
