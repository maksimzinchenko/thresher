import unittest
from validators import validate, MAX_FACTORIAL_VALUE

class TestCaseValidators(unittest.TestCase):

    def test_validate(self):
        self.assertRaises(ValueError, validate, "d")
        self.assertRaises(ValueError, validate, 1)
        self.assertRaises(ValueError, validate, False)
        self.assertRaises(ValueError, validate, {})
        self.assertRaises(ValueError, validate, {"number": "test"})
        self.assertRaises(ValueError, validate, {"task_id": 4})
        self.assertRaises(ValueError, validate, {"number": MAX_FACTORIAL_VALUE + 1})
        self.assertEqual(validate('{"test":"test"}'), {"test": "test"})
        self.assertEqual(validate('{"type":"factorial", "number": 1}'), {"type":"factorial", "number": 1})
