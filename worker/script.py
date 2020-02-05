from tasks import add
from celery import chain

# This nicely goes into the except clause and prints the error
try:
    r = add.delay(4, 4)
    r.get()
except Exception as e:
    print(e)

# This hangs indefinitely on c.get()
try:
    c = chain(add.s(4, 4), add.s(5, 5)).delay()
    c.get()
except Exception as e:
    print(e)
