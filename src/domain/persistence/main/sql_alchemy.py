"""
    ToDo: DocString
"""
import sys
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ROOT_DIRECTORY = str(Path(__file__).parents[3])
sys.path.append(f"{ROOT_DIRECTORY}")

from settings import AppSettings


settings = AppSettings()
engine = settings.get("MAIN.DATABASE.ENGINE")
host = settings.get("MAIN.DATABASE.HOST")
port = settings.get("MAIN.DATABASE.PORT")
user = settings.get("MAIN.DATABASE.USER")
password = settings.get("MAIN.DATABASE.PASSWORD")
database = settings.get("MAIN.DATABASE.NAME")

DATABASE_URL = f"{engine}://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

# sql_alchemy = SQLAlchemy()

# def set_connection(app: Flask) -> SQLAlchemy:
#     """ ToDo: DocString """
#     settings = AppSettings()
#     engine = settings.get("MAIN.DATABASE.ENGINE")
#     host = settings.get("MAIN.DATABASE.HOST")
#     port = settings.get("MAIN.DATABASE.PORT")
#     user = settings.get("MAIN.DATABASE.USER")
#     password = settings.get("MAIN.DATABASE.PASSWORD")
#     database = settings.get("MAIN.DATABASE.NAME")

#     app.config["SQLALCHEMY_DATABASE_URI"] = f"{engine}://{user}:{password}@{host}:{port}/{database}"
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

#     sql_alchemy.app = app
#     sql_alchemy.init_app(app)

#     return sql_alchemy
