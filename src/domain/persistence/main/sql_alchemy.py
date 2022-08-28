"""
    ToDo: DocString
"""
import sys
from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

ROOT_DIRECTORY = str(Path(__file__).parents[3])
sys.path.append(f"{ROOT_DIRECTORY}")

from settings import AppSettings

sql_alchemy = SQLAlchemy()

def set_connection(app: Flask) -> SQLAlchemy:
    """ ToDo: DocString """
    settings = AppSettings()
    engine = settings.get("MAIN.DATABASE.ENGINE")
    host = settings.get("MAIN.DATABASE.HOST")
    port = settings.get("MAIN.DATABASE.PORT")
    user = settings.get("MAIN.DATABASE.USER")
    password = settings.get("MAIN.DATABASE.PASSWORD")
    database = settings.get("MAIN.DATABASE.NAME")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"{engine}://{user}:{password}@{host}:{port}/{database}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    sql_alchemy.app = app
    sql_alchemy.init_app(app)

    return sql_alchemy
