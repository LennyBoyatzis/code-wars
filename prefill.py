import unittest

def prefill(n,v='undefined'):
    if n is []:
        return []

    if isinstance(n, str) and not n.isdigit():
        raise TypeError('{} is invalid'.format(n))

    if not isinstance(n, int) and n < 0:
        raise TypeError('{} is invalid'.format(n))

    return [v] * n

class TestPrefillFunction(unittest.TestCase):
    def test_err(self):
        self.assertRaises(TypeError, prefill, 'xyz', 1)

    def test_err_negative_n(self):
        self.assertRaises(TypeError, prefill, 'xyz', -1)

    def test_it_works_with_string(self):
        result = prefill(4, 'xyz')
        expected = ['xyz', 'xyz', 'xyz', 'xyz']
        self.assertEqual(result, expected)

    def test_it_works_with_integer(self):
        result = prefill(4, 1)
        expected = [1,1,1,1]
        self.assertEqual(result, expected)

    def test_it_works_no_v_arg(self):
        result = prefill(2)
        expected = ['undefined', 'undefined']
        self.assertEqual(result, expected)

    def test_return_empty_list_if_n_is_0(self):
        result = prefill(0, 'xyz')
        expected = []
        self.assertEqual(result, expected)

if __name__ == "__main__":
    print("Hello world")
