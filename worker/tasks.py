from celery import Celery
from celery.signals import task_postrun


app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@rabbit//')

@app.task
def add(x, y):
    import time
    time.sleep(5)
    return x + y


@task_postrun.connect
def task_postrun_handler(**kwargs):
    print("postrun handler", kwargs)
