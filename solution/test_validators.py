import unittest
from validators import validate

class TestCaseValidators(unittest.TestCase):

    def test_validate(self):
        self.assertRaises(ValueError, validate, "d")
        self.assertRaises(ValueError, validate, 1)
        self.assertRaises(ValueError, validate, False)
        self.assertRaises(ValueError, validate, {})
        self.assertEqual(validate('{"test":"test"}'), {"test": "test"})
