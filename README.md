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

Or build and run with Docker. The container applies migrations on startup.

```bash
touch db.sqlite3
docker compose up --build
```

On Linux the container runs as root, so the bind-mounted `db.sqlite3` can end up
root-owned and host-side commands such as `uv run python manage.py migrate`
cannot write it. Fix the ownership if that happens:

```bash
sudo chown "$(id -u):$(id -g)" db.sqlite3
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
