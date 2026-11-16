# studb

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9270511274ee4262be91474d9095e0b6)](https://app.codacy.com/manual/ymmmtym/studb?utm_source=github.com&utm_medium=referral&utm_content=ymmmtym/studb&utm_campaign=Badge_Grade_Dashboard)

```bash
APP=studb
PROJECT=studysite
```

## setup

Install dependencies with [uv](https://docs.astral.sh/uv/) (Python 3.12).

```bash
uv sync
```

Or build and run with Docker.

```bash
touch db.sqlite3
docker compose up --build
```

## operation

make migrations

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
uv run python manage.py createsuperuser
```

run server

```bash
uv run python manage.py runserver
```

delete migrations

```bash
cd ${APP}
rm -fr migrations

cd ${PROJECT}
rm -f db.sqlite3
```
