import unittest
import mycode

class TestMyCode(unittest.TestCase):
    def test_add(self):
        self.assertEqual(mycode.add(5, -8), 3)
        self.assertEqual(mycode.add(5, 3), 8)
        self.assertEqual(mycode.add(-5, -3), -8)