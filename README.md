# studb
```bash
APP=studb
PROJECT=studysite
```

## operation
make migrations
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

delete migrations
```bash
cd ${APP}
rm -fr migrations

cd ${PROJECT}
rm -f db.sqlite3
```