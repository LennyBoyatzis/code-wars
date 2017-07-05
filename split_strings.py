def solution(s):
    # return [s[i:i+2] for i in range(0, len(s), 2)]
    if len(s) % 2 == 0:
        return [s[i:i+2] for i in range(0, len(s), 2)]
    else:
        return [s[i:i+2] if i is not len(s) - 1 else s[i] + '_' for i in range(0, len(s), 2)]

if __name__ == "__main__":
    print(solution("hello_"))
