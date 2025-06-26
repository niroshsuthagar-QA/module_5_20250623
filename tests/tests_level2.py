import unittest
from python_app.calculator import Calculator

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.operation = Calculator(8,2)

    def test_sum(self):
        self.assertEqual(self.operation.get_sum(), 10, 'The sum is wrong')
    
    def test_diff(self):
        self.assertEqual(self.operation.get_difference(), 6, 'wrong')

    def test_product(self):
        self.assertEqual(self.operation.get_product(), 16, 'wrong')

    def test_quotient(self):
        self.assertEqual(self.operation.get_quotient(), 4, 'wrong')

    
if __name__ == '__main__':
    unittest.main()