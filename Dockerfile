FROM python:3.11-buster

RUN pip3 install poetry

WORKDIR /project
COPY pyproject.toml poetry.lock /project/

RUN poetry install --without dev

COPY . /project
EXPOSE 8000