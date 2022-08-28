"""
    ToDo: DocString
"""
import json
from typing import Any
from application.main.system_management.errors_log.commands.create_error_log import (
    CreateErrorLogVm)
from .api_result_vm import ApiResultVm
from .api_message_vm import ApiMessagesVm, ErrorMessage


class ApiResponseVm:
    """ ToDo: DocString """

    def __init__(self, content: Any = None):
        self.info = self.__set_info(content)
        self.result = self.__set_result(content)

    def __to_dict_in_lambda(self, obj: Any):
        """ ToDo: DocString """
        return obj.__dict__

    def __set_info(self, info_value: Any):
        """ ToDo: DocString """
        if hasattr(info_value, '__orig_class__'):
            del info_value.__orig_class__

        if not isinstance(info_value, CreateErrorLogVm):
            return info_value

        if info_value.status_code >= 500 and info_value.status_code < 600:
            return ApiMessagesVm(
                messages = [
                    ErrorMessage(row = 0,
                                error_in = "server",
                                description = "There was an unhandled error.")]
            )

        if info_value.status_code >= 400 and "(type=assertion_error)" in info_value.description:
            splited_descriptions = info_value.description.replace("(type=assertion_error)",
                                                              "").split("\n")
            splited_descriptions.pop(0)
            splited_descriptions = [item.strip() for item in splited_descriptions]

            errors_list = []
            for count, error_in in enumerate(splited_descriptions):
                if count % 2 == 0:
                    errors_list.append(
                        ErrorMessage(row = int(count / 2),
                                     error_in = f"client: '{error_in}'",
                                     description = splited_descriptions[count + 1]))

            return ApiMessagesVm(
                messages = errors_list
            )

        return ApiMessagesVm(
            messages = [
                ErrorMessage(row = 0,
                             error_in = "client",
                             description = info_value.description)]
        )

    def __set_result(self, info_value: Any):
        """ ToDo: DocString """
        if not isinstance(info_value, CreateErrorLogVm):
            return ApiResultVm()

        return ApiResultVm(
            status_code = info_value.status_code,
            is_exception = True,
            style = ""
        )

    @property
    def json_string(self):
        """ ToDo: DocString """
        return json.dumps(self.__dict__, default = self.__to_dict_in_lambda)

    @property
    def json_object(self):
        """ ToDo: DocString """
        return json.loads(self.json_string)
