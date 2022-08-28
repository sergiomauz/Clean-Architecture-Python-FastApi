"""
    ToDo: DocString
"""

import uuid
from mediatr import Mediator
from flask import Blueprint, Response, request
from common.utils import Constants
from application.main.system_management.people.commands.create_person import (
    CreatePersonCommand, CreatePersonVm, CreatePersonHandler)
from application.main.system_management.people.queries.get_person import (
    GetPersonQuery, GetPersonVm, GetPersonHandler)
from application.main.system_management.people.queries.search_people import (
    SearchPeopleQuery, SearchPeopleVm, SearchPeopleHandler)
from application.main.system_management.people.commands.update_person import (
    UpdatePersonCommand, UpdatePersonVm, UpdatePersonHandler)
from application.main.system_management.people.commands.delete_person import (
    DeletePersonCommand, DeletePersonVm, DeletePersonHandler)
from presentation.common import ApiResponseVm


people = Blueprint("people", __name__)
mediator = Mediator()


@people.route("/", methods=["POST"])
async def create_person():
    """ ToDo: DocString """
    command = CreatePersonCommand.new(request)
    application_view_model = await mediator.send_async(command)
    api_response_view_model = ApiResponseVm(application_view_model)

    return Response(
        response = api_response_view_model.json_string,
        status = api_response_view_model.result.status_code,
        mimetype = Constants.CONTENT_TYPE_JSON
    )

@people.route("/", methods=["GET"])
async def search_people():
    """ ToDo: DocString """
    query = SearchPeopleQuery.new(request)
    application_view_model = await mediator.send_async(query)
    api_response_view_model = ApiResponseVm(application_view_model)

    return Response(
        response = api_response_view_model.json_string,
        status = api_response_view_model.result.status_code,
        mimetype = Constants.CONTENT_TYPE_JSON
    )

@people.route("/<uid>", methods=["GET"])
async def read_person(uid: uuid):
    """ ToDo: DocString """
    query = GetPersonQuery.new(uid)
    application_view_model = await mediator.send_async(query)
    api_response_view_model = ApiResponseVm(application_view_model)

    return Response(
        response = api_response_view_model.json_string,
        status = api_response_view_model.result.status_code,
        mimetype = Constants.CONTENT_TYPE_JSON
    )

@people.route("/", methods=["PUT"])
async def update_person():
    """ ToDo: DocString """
    command = UpdatePersonCommand.new(request)
    application_view_model = await mediator.send_async(command)
    api_response_view_model = ApiResponseVm(application_view_model)

    return Response(
        response = api_response_view_model.json_string,
        status = api_response_view_model.result.status_code,
        mimetype = Constants.CONTENT_TYPE_JSON
    )

@people.route("/", methods=["DELETE"])
async def delete_person():
    """ ToDo: DocString """
    command = DeletePersonCommand.new(request)
    application_view_model = await mediator.send_async(command)
    api_response_view_model = ApiResponseVm(application_view_model)

    return Response(
        response = api_response_view_model.json_string,
        status = api_response_view_model.result.status_code,
        mimetype = Constants.CONTENT_TYPE_JSON
    )
