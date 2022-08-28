"""
    ToDo: DocString
"""
from typing import List
from dataclasses import dataclass


@dataclass
class ErrorMessage:
    """ ToDo: DocString """
    row: int = 0
    error_in: str = ""
    description: str = ""


@dataclass
class ApiMessagesVm:
    """ ToDo: DocString """
    messages: List[ErrorMessage] = None
