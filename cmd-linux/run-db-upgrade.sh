# For more information:
# https://flask-migrate.readthedocs.io/en/latest/

cd src/domain/persistence/main/db
flask db upgrade -d migrations
