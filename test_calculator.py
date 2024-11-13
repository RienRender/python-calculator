import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 2), 4)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(2, 2), 0)


    def test_multi(self):
        self.assertEqual(self.calc.multiply(1, 2), 2)
    
    def test_multi(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)

    def test_modu(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)

    def test_modu(self):
        self.assertEqual(self.calc.modulo(3, 2), 1)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()

