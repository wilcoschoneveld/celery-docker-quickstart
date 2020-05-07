from celery import Celery
from celery.signals import task_postrun
import numpy as np


app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@rabbit//')
app.conf.task_time_limit = 2


@app.task
def long_running_task():
    # this should take a couple of seconds
    return np.sum(np.random.rand(20000, 20000))


@task_postrun.connect
def task_postrun_handler(**kwargs):
    print("postrun handler", kwargs)
