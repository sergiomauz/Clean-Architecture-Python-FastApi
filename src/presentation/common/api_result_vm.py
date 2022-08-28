"""
    ToDo: DocString
"""

class ApiResultVm:
    """ ToDo: DocString """

    def __init__(self,
                 status_code: int = 200,
                 is_exception: bool = False,
                 style: str = ""):
        """ ToDo: DocString """

        self.status_code = status_code
        self.is_exception = is_exception
        self.style = style
        