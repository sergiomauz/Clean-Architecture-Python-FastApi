"""
    ToDo: DocString
"""
from mediatr import Mediator
from common.utils import str_yyyymmdd_t
from application.common.general import PagerVm
from domain.models.main.system_management import Person
from .query import SearchPeopleQuery
from .view_model import SearchPeopleVm


@Mediator.handler
class SearchPeopleHandler:
    """ ToDo: DocString """

    def handle(self, query: SearchPeopleQuery) -> PagerVm[SearchPeopleVm]:
        """ ToDo: DocString """
        total_items = Person.total_count(basic_search_parameters = query)
        if total_items > 0:
            people_list = Person.filter(basic_search_parameters = query)
            people_items = list(map(lambda item: SearchPeopleVm(
                    uid = str(item.uid),
                    name = item.name,
                    last_name = item.last_name,
                    created_at = str_yyyymmdd_t(item.created_at),
                    modified_at = str_yyyymmdd_t(item.modified_at)
                ), people_list))
        else:
            people_items = []

        search_people_vm = PagerVm[SearchPeopleVm](
            items = people_items,
            total_items = total_items,
            current_page = query.current_page,
            page_size = query.page_size
        )

        return search_people_vm
