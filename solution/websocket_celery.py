import asyncio
import json
from websockets.server import serve

from celeryqueue import app
from validators import validate
from solvers import get_factorial, get_result_waiter, get_result, send_response, get_send_factorial


async def handle_message(message, websocket):
    try:
        request = validate(message)
        if request['type'] == 'factorial':
            asyncio.create_task(get_send_factorial(websocket, request))
        elif request['type'] == 'result':
            await get_result(websocket, request, app)
        else:
            await send_response(websocket, {'type': 'error', 'result': 'Unknown task'})
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
