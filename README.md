# studb

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9270511274ee4262be91474d9095e0b6)](https://app.codacy.com/manual/ymmmtym/studb?utm_source=github.com&utm_medium=referral&utm_content=ymmmtym/studb&utm_campaign=Badge_Grade_Dashboard)

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