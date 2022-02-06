FROM ubuntu:20.04

RUN apt update && apt -y upgrade && apt -y install tzdata
ENV TZ=Asia/Tokyo

RUN apt -y install python3-pip python3-django libmysqlclient-dev && \
    python3 -m pip install PyMySQL mysqlclient pillow