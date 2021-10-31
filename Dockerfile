FROM python:3.9-slim


WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

ENV PYTHONUNBUFFERED 1


COPY . /app

# ENV PORT 8000
# gunicorn as app server 

# CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 3 core.wsgi:application

