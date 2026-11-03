import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add1(self):
        self.assertEqual(self.calc.add(3,4), 7)

    def test_add2(self):
        self.assertEqual(self.calc.add(-1,2), 1)

    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(4,3), 1)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(3,4), -1)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(-3,-5), 15)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(2,-5), -10)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(4,2), 2)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(-50, -2), 25)
    
    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(2,2), 0)

    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(9,-4), -3)

if __name__ == '__main__':
    unittest.main()