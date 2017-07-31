import re

def valid_parentheses(string):
    clean_str =  re.sub(r'[^\(\)]', '', string)
    pattern = r'\([^\) ^(]*\)'
    balanced_parens = re.search(pattern, clean_str)
    while re.search(pattern, clean_str):
        clean_str = re.sub(pattern, '', clean_str)
    return True if len(clean_str) == 0 else False

# def valid_parentheses(string):
#     cnt = 0
#     for char in string:
#         if char == '(': cnt += 1
#         if char == ')': cnt -= 1
#         if cnt < 0: return False
#     return True if cnt == 0 else False

if __name__ == "__main__":
    print(valid_parentheses("(((()()())))"))
    print(valid_parentheses("hi(hi)()"))
    print(valid_parentheses("hi())("))
