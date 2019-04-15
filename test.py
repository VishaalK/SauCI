import unittest
from add import add

class TestAdd(unittest.TestCase):
    def test_add_one_and_two(self):
        self.assertEqual(add(1,2), 3)

    def test_add_two_and_three(self):
        self.assertEqual(add(2,3), 4)

if __name__ == '__main__':
    unittest.main()

    