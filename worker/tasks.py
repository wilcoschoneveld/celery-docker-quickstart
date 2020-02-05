from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@rabbit//')

@app.task
def add(x, y):
    return x + y
