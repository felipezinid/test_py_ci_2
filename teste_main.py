import unittest
from main import add, subtract, multiply, divide

class TestMainFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)

    def test_divide(self):
        self.assertEqual(divide(8, 4), 2)
        with self.assertRaises(Error):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
