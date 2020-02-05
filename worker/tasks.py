import time
from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@rabbit//')

@app.task
def add(x, y):
    time.sleep(2)
    1 / 0
    return x + y
