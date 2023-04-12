import unittest

class TestFuelCalculation(unittest.TestCase):

    def test_calculate_fuel(self):
        masses = ["12\n", "14\n", "1969\n", "100756\n"]
        expected_fuel = 34241
        self.assertEqual(calculate_fuel(masses), expected_fuel)
        
        self.assertEqual(calculate_fuel(12), 2)
        self.assertEqual(calculate_fuel(14), 2)
        self.assertEqual(calculate_fuel(1969), 654)
        self.assertEqual(calculate_fuel(100756), 33583)

if __name__ == '__main__':
    unittest.main()
