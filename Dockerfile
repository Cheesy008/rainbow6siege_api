FROM python:3.8 AS base

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

FROM base AS dependencies

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

FROM dependencies AS build

WORKDIR /code
COPY . /code

FROM python:3.8-slim-buster

WORKDIR /code

COPY --from=dependencies /code/requirements.txt ./
COPY --from=dependencies /root/.cache /root/.cache

RUN pip install -r requirements.txt

COPY --from=build /code/ ./

CMD ["/bin/sh", "docker-entrypoint.sh"]