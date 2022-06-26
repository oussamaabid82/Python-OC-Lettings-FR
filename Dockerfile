# syntax=docker/dockerfile:1

FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /code

COPY requirements.txt /code/

RUN python -m pip install --upgrade pip && pip install --root-user-action=ignore
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "migrate"] 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]