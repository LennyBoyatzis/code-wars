from itertools import permutations

def perms(string):
     return list(set(''.join(p) for p in permutations(string)))

if __name__ == "__main__":
    result = perms('test')
