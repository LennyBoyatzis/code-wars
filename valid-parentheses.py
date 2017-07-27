import re

def valid_parentheses(string):
    clean_str =  re.sub(r'[^\(\)]', '', string)
    pattern = r'\([^\) ^(]*\)'
    balanced_parens = re.search(pattern, clean_str)
    while re.search(pattern, clean_str):
        clean_str = re.sub(pattern, '', clean_str)
    return True if len(clean_str) == 0 else False

if __name__ == "__main__":
    print(valid_parentheses("(((()()())))"))
    print(valid_parentheses("hi(hi)()"))
    print(valid_parentheses("hi())("))
