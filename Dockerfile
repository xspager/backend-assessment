# pull official base image
FROM python:3.9.1-alpine

# set work directory
WORKDIR /test_T10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
COPY requirements_prod.txt .
RUN pip install -r requirements.txt
RUN pip install -r requirements_prod.txt

# copy project
COPY . .
