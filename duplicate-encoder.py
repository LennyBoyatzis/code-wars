# Because count is being used 
# We have a loop within a loop 
# This makes it an O(n^2) method
# This method is concise and readable but could be more efficient
# really_long_test_string = ''.join(['a' for x in range(100)])
really_long_test_string = 'adfajshdval;cj.vncv.,ndfa.kds,nfasd.kjfhnad.kcj,ndk.jfhndsk.'

def duplicate_encode_0n2(word):
    word = word.lower()
    return ''.join(['(' if word.count(x) else ')' for x in word])

# The following is an O(n) method

import collections

def duplicate_encode_0n(word):
    new_string = ''
    word = word.lower()
    d = collections.defaultdict(int)
    for c in word:
        d[c] += 1
    for c in word:
        new_string = new_string + ('(' if d[c] == 1 else ')')
    return new_string

if __name__ == "__main__":
    import timeit

    # Test performance - duplicate_encode_0n2
    print(timeit.timeit("duplicate_encode_0n2(really_long_test_string)",
                        setup="from __main__ import duplicate_encode_0n2, really_long_test_string"))

    # Test performance - duplicate_encode_0n
    print(timeit.timeit("duplicate_encode_0n(really_long_test_string)",
                        setup="from __main__ import duplicate_encode_0n, really_long_test_string"))

