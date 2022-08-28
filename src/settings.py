"""
    ToDo: DocString
"""


import os
from dotenv import load_dotenv


class AppSettings:
    """ ToDo: DocString """

    def __init__(self):
        """ ToDo: DocString """
        load_dotenv()
        self.__value = os.environ

    def get(self, key: str) -> str:
        """ ToDo: DocString """
        return self.__value[key]
