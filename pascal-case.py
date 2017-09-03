import unittest

def to_underscore(string):
    return ''.join(['_{}'.format(letter.lower()) if letter.isupper() 
                    else letter.lower() for letter in string]).lstrip('_')


class TestToUnderscoreMethod(unittest.TestCase):
    def test_inputs_one(self):
        result = to_underscore('TestController')
        self.assertTrue(result, 'test_controller')

    def test_inputs_two(self):
        result = to_underscore('MoviesAndBooks')
        self.assertTrue(result, 'movies_and_books')

    def test_inputs_three(self):
        result = to_underscore('App7Test')
        self.assertTrue(result, 'app7_test')

if __name__ == "__main__":
    print("Hello world")
