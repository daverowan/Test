import unittest
from compute_stats2 import compute_stats


class TestComputeStats(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(compute_stats([]), (None, None, None, None))

    def test_single_element(self):
        self.assertEqual(compute_stats([5]), (5, 5, 5, 5))

    def test_even_number_of_elements(self):
        self.assertEqual(compute_stats([1, 3, 5, 7]), (1, 7, 4, 4))

    def test_odd_number_of_elements(self):
        self.assertEqual(compute_stats([1, 3, 5]), (1, 5, 3, 3))

    def test_unsorted_list(self):
        self.assertEqual(compute_stats([7, 1, 5, 3]), (1, 7, 4, 4))


if __name__ == '__main__':
    unittest.main()