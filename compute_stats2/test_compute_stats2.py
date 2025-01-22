import unittest
from compute_stats2 import calculate_stats  # Import the function to test


class TestComputeStats(unittest.TestCase):
    """Unit tests for the calculate_stats function."""

    def test_even_number_of_elements(self):
        """Test with a list containing an even number of elements."""
        values = [2, 4, 6, 8]
        result = calculate_stats(values)
        self.assertEqual(result, (2, 8, 5, 5))  # min, max, average, median

    def test_odd_number_of_elements(self):
        """Test with a list containing an odd number of elements."""
        values = [1, 3, 5, 7, 9]
        result = calculate_stats(values)
        self.assertEqual(result, (1, 9, 5, 5))  # min, max, average, median

    def test_empty_list(self):
        """Test with an empty list."""
        values = []
        result = calculate_stats(values)
        self.assertIsNone(result)  # Should return None for all values

    def test_single_element(self):
        """Test with a list containing a single element."""
        values = [42]
        result = calculate_stats(values)
        self.assertEqual(result, (42, 42, 42, 42))  # min, max, average, median

    def test_large_range(self):
        """Test with a list containing a wide range of values."""
        values = [1, 1000, 500, 250, 750]
        result = calculate_stats(values)
        self.assertEqual(result, (1, 1000, 500, 500))  # min, max, average, median


if __name__ == "__main__":
    unittest.main()
