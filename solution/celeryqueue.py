from celery import Celery

app = Celery('celeryqueue',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0',
             result_backend='redis://localhost:6379/0',
             include=['tasks'])

app.conf.task_routes = ([
    {'tasks.factorial_task': {'queue': 'soft'}},
    {'tasks.factorial_task1000': {'queue': 'hard'}},
])

app.conf.update(
    result_expires=3600,
)
