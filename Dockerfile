FROM python:3.10-alpine3.16

COPY requirements.txt /temp/requirements.txt
# RUN apk add postgresql-client build-base postgresql-dev
RUN apk update && apk add python3-dev \
                          gcc \
                          libc-dev \
                          libffi-dev \
RUN apt-get update && apt-get install -y libpq-dev build-essential
RUN pip install -r /temp/requirements.txt --no-cache-dir
RUN adduser --disabled-password backend-user

COPY backend /backend
WORKDIR /backend
EXPOSE 8000

USER backend-user
