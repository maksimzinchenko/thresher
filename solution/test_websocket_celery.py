import asyncio
import json
import unittest
from websockets.client import connect

class TestWebSocketServer(unittest.IsolatedAsyncioTestCase):
    async def test_websocket_server(self):
        async with connect('ws://localhost:25000') as websocket:
            # Send factorial of 5 request to server
            test_factorial_5 = {"type": "factorial", "number":5}
            await websocket.send(json.dumps(test_factorial_5))

            # Receive first response from server with ticket
            response1 = await websocket.recv()
            expected_response1 = {"type": "result", "task_id": "some id"}
            decoded_response1 = json.loads(response1)
            self.assertEqual(decoded_response1["type"], expected_response1["type"])
            self.assertIsInstance(decoded_response1["task_id"], str)

            # Receive second response from server with result answer
            response2 = await websocket.recv()
            expected_response2 = {"type": "success", "task_id": "some id", "result": 120}
            decoded_response2 = json.loads(response2)
            self.assertEqual(decoded_response2["type"], expected_response2["type"])
            self.assertEqual(decoded_response1["task_id"], decoded_response2["task_id"])
            self.assertEqual(decoded_response2["result"], expected_response2["result"])