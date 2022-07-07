# syntax=docker/dockerfile:1

FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN python -m pip install --user --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /code/

EXPOSE 8000

CMD  python manage.py migrate && python manage.py runserver 127.0.0.1:$PORT --insecure