"""
    ToDo: DocString
"""
import sys
from pathlib import Path
from flask import Flask
from flask_migrate import Migrate

ROOT_DIRECTORY = str(Path(__file__).parents[5])
sys.path.append(f"{ROOT_DIRECTORY}/src/")

from domain.persistence.main import set_connection
from domain.models.main.system_management import (
    Person, ErrorLog)


app = Flask(__name__)
db = set_connection(app)
migrate = Migrate(app, db)
