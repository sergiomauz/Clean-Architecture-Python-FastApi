"""
    ToDo: DocString
"""
from mediatr import Mediator
from flask import Response
from common.utils import Constants
from presentation.common import ApiResponseVm
from application.main.system_management.errors_log.commands.create_error_log import (
    CreateErrorLogCommand, CreateErrorLogVm, CreateErrorLogHandler)


class CustomExceptionsHandler:
    """ ToDo: DocString """

    def start_custom_exceptions(self, app):
        """ ToDo: DocString """
        app.register_error_handler(Exception, self.api_error_response)

    def api_error_response(self, exception):
        """ ToDo: DocString """
        mediator = Mediator()
        command = CreateErrorLogCommand(exception)
        error_view_model = mediator.send(command)
        api_response_view_model = ApiResponseVm(error_view_model)

        return Response(
            response = api_response_view_model.json_string,
            status = api_response_view_model.result.status_code,
            mimetype = Constants.CONTENT_TYPE_JSON
        )
