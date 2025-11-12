# https://github.com/AnaisM7/lab11-AM-EB.git
# Partner 1: Anais Maldonado
# Partner 2: Emy Bijoy

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-2, -2), 0)
    ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 5), 15)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(0, 11), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(5, 15), 3)
        self.assertEqual(div(2,20), 10)
        with self.assertRaises(ZeroDivisionError):
            div(0, 7)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(10, 1000), 3.0)
        self.assertAlmostEqual(logarithm(math.e, math.e ** 2), 2.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 10)
    # ##########################

    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(1.5, 2.5), math.hypot(1.5, 2.5))

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(4), 2.0)
        self.assertEqual(square_root(9), 3.0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()