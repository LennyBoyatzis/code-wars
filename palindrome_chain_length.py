def palindrome_chain_length(n):
    str_num = str(n)
    str_num_rev = str(n)[::-1]
    steps = 0

    while str_num != str_num_rev:
        steps += 1
        increment = int(str_num) + int(str_num_rev)
        str_num = str(increment)
        str_num_rev = str(increment)[::-1]
    return steps




if __name__ == "__main__":
    print(palindrome_chain_length(87))
