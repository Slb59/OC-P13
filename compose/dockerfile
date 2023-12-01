FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY ./compose/requirements.txt .

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential && pip install -r requirements.txt

COPY . .

COPY ./compose/start /start
RUN sed -i 's/\r$//g' /start && chmod +x /start

RUN mkdir -p /app/logs