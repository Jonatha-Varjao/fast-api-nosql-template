FROM python:3.7-slim

RUN apt-get update -y && apt-get install -y python3-dev gcc
RUN python -m pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile /tmp/

RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./app /app
COPY .env .env
EXPOSE 80
CMD gunicorn -k uvicorn.workers.UvicornWorker -w 3 app.main:app -b 0.0.0.0:80
