FROM python:3.7-slim-buster
ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV worker_cmd="celery -A tasks worker --loglevel=info"
CMD sh run.sh
