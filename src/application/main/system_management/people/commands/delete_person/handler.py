"""
    ToDo: DocString
"""
from flask import abort
from mediatr import Mediator
from common.utils import Messages
from domain.models.main.system_management import Person
from .command import DeletePersonCommand
from .view_model import DeletePersonVm


@Mediator.handler
class DeletePersonHandler:
    """ ToDo: DocString """

    def handle(self, command: DeletePersonCommand) -> DeletePersonVm:
        """ ToDo: DocString """
        people = Person.get_list_by_uids(uids_list = command.uids)
        if len(people) != len(command.uids):
            abort(status = 404, description = Messages.ID_NOT_FOUND)
        Person.delete_list_by_uids(uids_list = command.uids)

        delete_person_vm = DeletePersonVm(
            were_deleted = True)

        return delete_person_vm
