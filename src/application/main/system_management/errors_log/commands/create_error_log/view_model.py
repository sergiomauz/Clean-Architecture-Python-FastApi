"""
    ToDo: DocString
"""

from datetime import datetime


class CreateErrorLogVm:
    """ ToDo: DocString """

    def __init__(self,
                 status_code: str = None,
                 description: str = None,
                 stack_trace: str = None,
                 created_at: datetime = None) -> None:
        """ ToDo: DocString """

        self.status_code = status_code
        self.description = description
        self.stack_trace = stack_trace
        self.created_at = (created_at.isoformat() if created_at is not None else None)
