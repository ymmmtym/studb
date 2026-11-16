FROM ghcr.io/astral-sh/uv:0.13.7 AS uv

FROM python:3.12-slim
LABEL Maintainer="ymmmtym"
ENV HOSTNAME="studb" \
    APP="/app/studb" \
    PS1="[\u@\h \W]# " \
    UV_PROJECT_ENVIRONMENT="/app/studb/.venv" \
    PATH="/app/studb/.venv/bin:$PATH"

COPY --from=uv /uv /uvx /bin/

COPY [".", "${APP}"]
WORKDIR ${APP}
RUN uv venv && \
    uv pip install -r requirements.txt

EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0:8000" ]
