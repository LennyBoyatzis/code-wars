# Test Fixture - A fixture is used to setup a test (create and teardown)
# Test Case - Actual test
# Test Suite - Collection of Test Cases
# Test Runner - Orchestrates the runnning of tests or suites

import mymath
import unittest

class TestAdd(unittest.TestCase):
    '''
    Test the add function from the mymath lib
    '''
    def test_add_integers(self):
        '''
        Test that the addition of two integers returns the correct total
        '''
        result = mymath.add(1,2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        '''
        Test that the addition of two integers returns the correct total
        '''
        result = mymath.add(10.5,2)
        self.assertEqual(result, 12.5)

if __name__ == "__main__":
