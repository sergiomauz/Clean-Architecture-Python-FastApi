"""
    ToDo: DocString
"""
from flask import Flask
from domain.persistence.main import set_connection, sql_alchemy
from presentation.routes import RoutesHandler
from presentation.exceptions import CustomExceptionsHandler


app = Flask(__name__)
db = set_connection(app)

routes_handler = RoutesHandler()
routes_handler.start_routes(app)

exceptions_handler = CustomExceptionsHandler()
exceptions_handler.start_custom_exceptions(app)


if __name__ == "__main__":
    app.run(debug = True)
