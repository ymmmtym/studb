FROM python:3.7.5
LABEL Maintainer "ymmmtym"
ENV HOSTNAME="studb-container" \
    APP_PATH="/app" \
    PS1="[\u@\h \W]# "

COPY ["requirements.txt", "/tmp"]
COPY ["app", "$APP_PATH"]
WORKDIR $APP_PATH
RUN apt-get update && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install -r /tmp/requirements.txt

EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0:8000" ]
