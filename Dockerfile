FROM python:3.10-alpine3.16

COPY requirements.txt /temp/requirements.txt
# RUN apk add postgresql-client build-base postgresql-dev
RUN pip install --upgrade pip
RUN apk update && apk add python3-dev \
                          gcc \
                          libc-dev \
                          libffi-dev \
    && pip install --no-cache-dir -r /temp/requirements.txt
RUN adduser --disabled-password backend-user

COPY backend /backend
WORKDIR /backend
EXPOSE 8000

USER backend-user
