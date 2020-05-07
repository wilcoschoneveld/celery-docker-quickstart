# Celery Docker Quickstart

Celery worker in docker with auto reloading on code changes.


Use the following in a terminal to start a worker:

        docker-compose up worker

Run a task with this example command:

        docker-compose run worker python script.py 10 20
