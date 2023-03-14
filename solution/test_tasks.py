import unittest
from tasks import factorial_task, factorial_task1000
import math

class TestCaseTasks(unittest.TestCase):

    def test_factorial_task(self):
        self.assertEqual(factorial_task(0), math.factorial(0))
        self.assertEqual(factorial_task(5), math.factorial(5))
        self.assertEqual(factorial_task(100), math.factorial(100))