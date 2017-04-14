def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for
                     word in title])

if __name__ == "__main__":
    print(title_case('a clash of KINGS', 'a an the of'));
    print(title_case('THE WIND IN THE WILLOWS', 'The In'));
    print(title_case('the quick brown fox', 'The Quick Brown Fox'));
