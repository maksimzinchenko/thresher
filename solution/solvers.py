import json
import asyncio
from celery.result import AsyncResult

from tasks import factorial_task, factorial_task1000, HARD_TASK_TIMEOUT


async def get_factorial(request):
    task = None
    if request['number'] < 1000:
        task = factorial_task.delay(request['number'])
    else:
        task = factorial_task1000.delay(request['number'])
    return task


async def send_response(websocket, response):
    await websocket.send(json.dumps(response))


async def get_result_waiter(websocket, task):
    loop = asyncio.get_running_loop()
    end_time = loop.time() + HARD_TASK_TIMEOUT
    while True:
        if loop.time() >= end_time:
            await send_response(websocket, {'type': 'error', 'result': 'Timeout error'})
            break
        if task.status == 'SUCCESS':
            await send_response(websocket, {'type': 'success',
                                            'task_id': str(task.task_id),
                                            'result': task.get()})
            break
        await asyncio.sleep(0.1)


async def get_result(websocket, request, app):
    task_id = request['task_id']
    result = AsyncResult(task_id, app=app)
    if result.ready():
        await send_response(websocket, {'type': 'result', 'result': result.result})
    else:
        await send_response(websocket, {'type': 'result', 'result': result.status})
