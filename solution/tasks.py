import math
#import time

from celeryqueue import app

SOFT_TASK_TIMEOUT = 10
HARD_TASK_TIMEOUT = 60


@app.task(time_limit=SOFT_TASK_TIMEOUT)
def factorial_task(message):
    return math.factorial(int(message))

@app.task(time_limit=HARD_TASK_TIMEOUT)
def factorial_task1000(message):
    #start = time.time()
    x = math.factorial(int(message))
    #end = time.time()
    #delta = end - start
    #print("calc took %.2f seconds to process" % delta)
    return  x
