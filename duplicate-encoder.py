def duplicate_encode(word):
    char_more_than_once = lambda char: word.count(char) > 1 
    return ''.join([')' if char_more_than_once(char) else '(' for char
                    in word.lower()])

if __name__ == "__main__":
    print(duplicate_encode("din"))
    print(duplicate_encode("recede"))
    print(duplicate_encode("Success"))
    print(duplicate_encode("(( @"))

