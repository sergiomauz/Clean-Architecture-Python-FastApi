"""
    ToDo: DocString
"""
import traceback
from typing import Any
from pydantic import ValidationError
from werkzeug.exceptions import NotFound


class CreateErrorLogCommand:
    """ ToDo: DocString """

    def __init__(self, exception: Any = None):
        """ ToDo: DocString """
        self.description = exception.__dict__.get("description", str(exception))
        self.stack_trace = "".join(traceback.format_tb(exception.__traceback__))
        # self.context = context

        if isinstance(exception, ValidationError):
            self.status_code = 400
        elif isinstance(exception, NotFound):
            self.status_code = 404
        else:
            self.status_code = 500
