"""
    ToDo: DocString
"""
from dataclasses import dataclass
from application.common.general import BasicViewModel


@dataclass
class CreatePersonVm(BasicViewModel):
    """ ToDo: DocString """
    name: str = None
    last_name: str = None
