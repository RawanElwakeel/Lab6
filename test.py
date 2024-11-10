import unittest
from main import add_number
class TestAddNumber(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_number(4, 2), 6)
        self.assertEqual(add_number(2, 1), 3)
        self.assertEqual(add_number(14, 1), 15)

if __name__ == "__main__":
    unittest.main()
