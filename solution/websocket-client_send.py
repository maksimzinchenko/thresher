#!/usr/bin/env python

import asyncio
from websockets.client import connect
import json


async def hello():
    async with connect('ws://localhost:25000') as websocket:
        number = input("Input factorial number? ")

        await websocket.send(json.dumps({"type": "factorial", "number": int(number)}))
        print(f"> {number}")

        factorial_result = json.loads(await websocket.recv())
        print(f"{str(factorial_result)}")

asyncio.get_event_loop().run_until_complete(hello())
