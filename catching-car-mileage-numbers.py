from functools import reduce

def is_palindrome(string):
    return string == string[::-1]

def is_seq_inc(string):
    return ''.join(list(string).sort()) == string

def is_seq_dec(string):
    return ''.join(list(string).sort(reverse=True)) == string

def is_awesome_phrase(string, phrases):
    for phrase in phrases:
        if string == phrase:
            return True
    return False

def all_digits_same(string):
    return string == len(string) * string[0]

def digit_followed_by_zeroes(string):
    return string[1:] == (len(string) - 1) * '0'

def is_interesting(number, awesome_phrases):
    function_list = [
        is_palindrome,
        is_seq_inc,
        is_seq_dec,
        is_awesome_phrase,
        all_digits_same,
        digit_followed_by_zeroes
    ]
    return reduce((lambda x, y: y(x)), function_list, str(number))


if __name__ == "__main__":
    print(is_interesting(11207, [])) # 0
    # is_interesting(11208, []) # 0
    # is_interesting(11209, []) # 1
    # is_interesting(11210, []) # 1
    # is_interesting(11211, []) # 2
