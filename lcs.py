import unittest
from collections import Counter

def lcs(x, y):
    counter_x = Counter(x)
    counter_y = Counter(y)
    common_letters = list((counter_x & counter_y).elements())
    return ''.join(sorted(common_letters))

class TestLCSMethod(unittest.TestCase):
    def test_returns_a_string(self):
        result = lcs('hello', 'ello')
        self.assertTrue(isinstance(result, str))

    def test_return_a_subset_of_string(self):
        result = lcs('hello', 'ello')
        self.assertEqual(result, 'ello')

if __name__ == "__main__":
    print("script is running", lcs('hello', 'ello'))
