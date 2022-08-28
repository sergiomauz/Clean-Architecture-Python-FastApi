"""
    ToDo: DocString
"""
import math
from typing import Generic, List, TypeVar


T = TypeVar("T")


class PagerVm(Generic[T]):
    """ ToDo: DocString """

    def __init__(self,
                 items: List[T] = None,
                 total_items: int = 0,
                 current_page: int = 1,
                 page_size: int = 10) -> None:
        """ ToDo: DocString """

        self.total_items = total_items
        self.current_page = current_page

        if page_size > 0:
            self.page_size = page_size
            self.total_pages = int(math.ceil(self.total_items / self.page_size))
            if self.total_pages == 0:
                self.total_pages = 1
        else:
            self.page_size = total_items
            self.total_pages = 1

        self.first_item = self.page_size * (self.current_page - 1) + 1
        if self.total_items > self.page_size * self.current_page:
            self.last_item = self.page_size * self.current_page
        else:
            self.last_item = self.total_items
        if items is not None:
            self.items = items
        else:
            self.items = []
