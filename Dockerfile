FROM python:3.9.7-alpine

WORKDIR /app

COPY . .

# RUN pip3 install -r requirements.txt

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir --upgrade -r requirements.txt


RUN python manage.py makemigrations && \
    python manage.py migrate


ENV PORT 8000

CMD gunicorn --bind :$PORT --workers 3 core.wsgi:application