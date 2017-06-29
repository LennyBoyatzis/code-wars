from collections import Counter
from sys import getsizeof

# Simple Timers
# Using the timeit module

def scramble_linear(s1, s2):
    return len(Counter(s1) - Counter(s2)) == 0

def scramble_on2(s1, s2):
    for letter in s2:
        if letter not in s1:
            return False

    return True

if __name__ == "__main__":
    import cProfile
    cProfile.runctx('scramble_on2(s1,s2)', {'s1':
                                            'rkqodlsdfadsfasdfsdfasdfasdfasdfdsafsadfasdfadsfasdfasdfasdfsdafasdfsdw',
                                            's2': 'work'}, {})
