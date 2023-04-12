import unittest


class TestCalculateFuel(unittest.TestCase):
    def test_calculate_fuel(self):
        masses = [12, 14, 1969, 100756]
        expected_fuel = 5
        self.assertEqual(calculate_fuel(masses), expected_fuel)

        self.assertEqual(calculate_fuel([14]), 2)
        self.assertEqual(calculate_fuel([1969]), 966)
        self.assertEqual(calculate_fuel([100756]), 50346)




if __name__ == '__main__':
    unittest.main()
