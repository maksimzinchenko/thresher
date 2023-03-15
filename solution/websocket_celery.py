import asyncio
import json
from websockets.server import serve

from celeryqueue import app
from validators import validate
from solvers import get_factorial, get_result_waiter, get_result, send_response


async def handle_message(message, websocket):
    try:
        request = validate(message)
        if request['type'] == 'factorial':
            task = await get_factorial(request)
            await send_response(websocket, {'type': 'result', 'task_id': task.id})
            await get_result_waiter(websocket, task)
            return {"type": "factorial", "result": "success"}
        elif request['type'] == 'result':
            await get_result(websocket, request, app)
            return {"type": "result", "result": "success"}
        else:
            await send_response(websocket, {'type': 'error', 'result': 'Unknown task'})
            return {"type": "error", "result": "Unknown request"}
    except ValueError:
        response = {'type': 'error', 'result': 'Request validation error'}
        await send_response(websocket, response)
    except:
        print("Something else went wrong")
        response = {'type': 'error', 'result': 'Common error'}
        await send_response(websocket, response)


async def consumer_handler(websocket):
    async for message in websocket:
        await handle_message(message, websocket)


async def server():
    async with serve(consumer_handler, "localhost", 25000):
        await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(server())
