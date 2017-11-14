from itertools import permutations
from itertools import combinations
from itertools import chain

# Generates all possible ways of ordering a set of things
for p in permutations([1,2,3]):
    print(p)

# Generates all possibles ways of selecting items from a collection
for c in combinations([1,2,3,4], 2):
    print(c)

# Takes iterables and creates a new iterator that returns elements from 
# the given iterables sequentially, as a single sequence
for c in chain(range(3), range(12, 15)):
    print(c)
