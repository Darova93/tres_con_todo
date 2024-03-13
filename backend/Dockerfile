# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /code
COPY requirements.txt /code
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

RUN pip3 install debugpy

COPY . .

ENV FLASK_APP app.py
ENV FLASK_ENV development
ENV FLASK_RUN_PORT 8000
ENV FLASK_RUN_HOST 0.0.0.0

EXPOSE 8000

CMD ["flask", "run"]

FROM builder AS dev-envs

CMD ["python", "app.py"]

FROM builder AS dev-envs-debug

EXPOSE 5678

CMD ["python", "-m", "debugpy", "--wait-for-client", "--listen", "0.0.0.0:5678", "-m", "flask", "run"]
