"""
    ToDo: DocString
"""
from mediatr import Mediator
from common.utils import str_yyyymmdd_t
from domain.models.main.system_management import Person
from .command import CreatePersonCommand
from .view_model import CreatePersonVm


@Mediator.handler
class CreatePersonHandler:
    """ ToDo: DocString """

    def handle(self, command: CreatePersonCommand) -> CreatePersonVm:
        """ ToDo: DocString """
        person = Person(
            name = command.name,
            last_name = command.last_name)
        person.save()

        create_person_vm = CreatePersonVm(
            uid = str(person.uid),
            name = person.name,
            last_name = person.last_name,
            created_at = str_yyyymmdd_t(person.created_at),
            modified_at = str_yyyymmdd_t(person.modified_at))

        return create_person_vm
