# studb
```
APP=studb
PROJECT=studysite
```

## operation
make migrations
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

```

delete migrations
```
cd ${APP}
rm -fr migrations

cd ${PROJECT}
rm -f db.sqlite3

```