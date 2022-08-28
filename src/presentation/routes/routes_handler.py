"""
    ToDo: DocString
"""


from common.utils import Constants
from presentation.routes.system_management import people


class RoutesHandler:
    """ ToDo: DocString """
    def start_routes(self, app):
        """ ToDo: DocString """
        module_system = f"{Constants.API_V1}/system"

        app.register_blueprint(people,
                               url_prefix = f"{module_system}/people")
