FROM python:3.7-alpine
LABEL Maintainer "ymmmtym"
ENV HOSTNAME="studb-container" \
    APP_PATH="/app" \
    PS1="[\u@\h \W]# "

COPY ["requirements.txt", "/tmp"]
COPY ["app", "$APP_PATH"]
WORKDIR $APP_PATH
RUN apk update && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install -r /tmp/requirements.txt

EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0:8000" ]
