import unittest

from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(Subtract(8, 6), 2)

if __name__ == '__main__':
    unittest.main()
