"""
    ToDo: DocString
"""
import os
from datetime import datetime
from mediatr import Mediator
from common.utils import Constants, str_yyyymmdd_t
from domain.models.main.system_management import ErrorLog
from domain.persistence.main import sql_alchemy as db
from .command import CreateErrorLogCommand
from .view_model import CreateErrorLogVm


@Mediator.handler
class CreateErrorLogHandler:
    """ ToDo: DocString """

    def __save_error_in_file(self, command: CreateErrorLogCommand) -> None:
        """ ToDo: DocString """
        now = datetime.now()
        folder_name = f"{Constants.ERRORS_LOG_DIRECTORY}/{now.strftime('%Y-%m')}"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        str_error = "===============================================================\n"
        str_error = str_error + f"{str_yyyymmdd_t(now)}\n"
        str_error = str_error + "Error caught in this application handler\n"
        str_error = str_error + f"Status Code: {command.status_code}\n"
        str_error = str_error + f"Error Message: {command.description}\n"
        str_error = str_error + f"Stack Trace: {command.stack_trace}\n"
        str_error = str_error + "===============================================================\n"
        with open(f"{folder_name}/{now.strftime('%Y-%m-%d')}.txt", "a+",
                  encoding="utf-8") as file_object:
            file_object.seek(0)
            file_object.write(str_error)
            file_object.close()

    def handle(self, command: CreateErrorLogCommand) -> CreateErrorLogVm:
        """ ToDo: DocString """
        error_log = ErrorLog(
            status_code = command.status_code,
            description = command.description,
            stack_trace = command.stack_trace)

        if error_log.status_code != 400:
            try:
                error_log.save()
            except:
                self.__save_error_in_file(command = command)

        create_error_log_vm = CreateErrorLogVm(
            status_code = error_log.status_code,
            description = error_log.description,
            stack_trace = error_log.stack_trace,
            created_at = error_log.created_at)

        return create_error_log_vm
