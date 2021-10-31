FROM python:3.9.7-alpine

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt


ENV PORT 8000

CMD gunicorn --bind :$PORT --workers 3 core.wsgi:application