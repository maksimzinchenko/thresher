import asyncio
import unittest

from tasks import SOFT_TASK_TIMEOUT

async def my_func():
    await asyncio.sleep(0.1)
    return True

class TestFactorialsSolution(unittest.IsolatedAsyncioTestCase):

    pass