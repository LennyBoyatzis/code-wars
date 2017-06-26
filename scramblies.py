from collections import Counter

def scramble(s1, s2):
    return len(Counter(s1) - Counter(s2)) == 0

if __name__ == "__main__":
    print(scramble('rkqodlw', 'work'))
