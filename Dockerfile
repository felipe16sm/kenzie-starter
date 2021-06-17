# imagem base
FROM python:3.8

COPY ./requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1

RUN apt update \
    && apt install -y libpq-dev gcc nano

RUN pip install psycopg2 coverage

WORKDIR /code
COPY . /code/
