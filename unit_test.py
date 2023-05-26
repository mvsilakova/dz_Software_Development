import math
import unittest
# Силакова Мария Вячеславовна, варинант 21, группа 44-22-114
def convert_value(x):
    if x < 3:
        y = x * math.cos(x**3) + x
    else:
        y = math.sqrt(x) * math.cos(0.0421 * x**2)
    return y

class ConvertValueTestCase(unittest.TestCase):
    def test_less_than_3(self):
        result = convert_value(2)
        expected = 2 * math.cos(2**3) + 2
        self.assertAlmostEqual(result, expected)

    def test_greater_than_or_equal_to_3(self):
        result = convert_value(5)
        expected = math.sqrt(5) * math.cos(0.0421 * 5**2)
        self.assertAlmostEqual(result, expected)

    def test_zero(self):
        result = convert_value(0)
        expected = 0 * math.cos(0**3) + 0
        self.assertAlmostEqual(result, expected)

if __name__ == '__main__':
    unittest.main()