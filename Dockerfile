FROM python:3.7.5
LABEL Maintainer="ymmmtym"
ENV HOSTNAME="studb" \
    APP="/app/studb" \
    PS1="[\u@\h \W]# "

COPY [".", "${APP}"]
WORKDIR ${APP}
RUN apt-get update && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install -r requirements.txt

EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0:8000" ]
