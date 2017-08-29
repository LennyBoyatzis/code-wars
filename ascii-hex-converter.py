import unittest

class Converter():

    @staticmethod
    def to_ascii(h):
        return str(h).decode('hex')
    @staticmethod
    def to_hex(s):
        return str(s).encode('hex')

class TestConverterClass(unittest.TestCase):
    def test_to_ascii_method(self):
        hex_string = '4c6f6f6b206d6f6d2c206e6f2068616e6473'
        result = Converter.to_ascii(hex_string)
        expected = 'Look mom, no hands'
        self.assertEqual(result, expected)

    def test_to_hex_method(self):
        ascii_string = 'Look mom, no hands'
        result = Converter.to_hex(ascii_string)
        expected = '4c6f6f6b206d6f6d2c206e6f2068616e6473'
        self.assertEqual(result, expected)

# FYI

# @classmethod
# with @classmethod, the object instance is
# implicitly passed as the first argument instead of self
# If you define something as class method it is probably
# because you intend to call it from the class rather than a class
# instance

# @staticmethod
# neither self nor class are implicitly passed as the
# first argument
# The behave like plain functions expect that you call them from
# an instance or the class
# It is callable without instantiating the class
