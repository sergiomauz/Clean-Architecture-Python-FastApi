# For more information:
# https://flask-migrate.readthedocs.io/en/latest/

len=0
while ((len<=0))
do
    read -p "Migration's name: " name
    len=`expr length "$name"`
done

cd src/domain/persistence/main/db
flask db migrate -d migrations -m "$name"
