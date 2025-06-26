import unittest
from python_app.calculator import Calculator

class TestOperations(unittest.TestCase):

    def test_sum(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.get_sum(), 10, 'The sum is wrong')
    
    def test_diff(self):
        calculation = Calculator(10,6)
        self.assertEqual(calculation.get_difference(), 4, 'wrong')

    def test_product(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.get_product(), 16, 'wrong')

    def test_quotient(self):
        calculation = Calculator(10,2)
        self.assertEqual(calculation.get_quotient(), 5, 'You are being silly')

    
if __name__ == '__main__':
    unittest.main()