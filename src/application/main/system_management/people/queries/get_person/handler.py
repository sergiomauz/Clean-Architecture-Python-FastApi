"""
    ToDo: DocString
"""
from flask import abort
from mediatr import Mediator
from common.utils import Messages, str_yyyymmdd_t
from domain.models.main.system_management import Person
from .query import GetPersonQuery
from .view_model import GetPersonVm


@Mediator.handler
class GetPersonHandler:
    """ ToDo: DocString """

    def handle(self, query: GetPersonQuery) -> GetPersonVm:
        """ ToDo: DocString """
        person = Person.get_by_uid(str_uid = query.uid)
        if not person:
            abort(status = 404, description = Messages.ID_NOT_FOUND)

        get_person_vm = GetPersonVm(
            uid = str(person.uid),
            name = person.name,
            last_name = person.last_name,
            created_at = str_yyyymmdd_t(person.created_at),
            modified_at = str_yyyymmdd_t(person.modified_at))

        return get_person_vm
