import unittest
from main import add, subtract, multiply, divide, modulus

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertEqual(add(3, 7), 10)

    def test_subtract(self):
        self.assertEqual(subtract(2, 5), -3)
        self.assertEqual(subtract(3, 7), -4)

    def test_multiply(self):
        self.assertEqual(multiply(2, 5), 10)
        self.assertEqual(multiply(3, 7), 20)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(14, 7), 2)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 3, 0)


    def test_modulus(self):
        self.assertEqual(modulus(5, 2), 1)
        self.assertEqual(modulus(10, 5), 0)

    def test_modulus_by_zero(self):
        self.assertRaises(ValueError, modulus, 10, 0)


if __name__ == '__main__':
    unittest.main()
