import sys
from tasks import add

a = int(sys.argv[1])
b = int(sys.argv[2])

r = add.delay(a, b)
