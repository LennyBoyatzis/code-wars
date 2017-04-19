def in_array(array1, array2):
    substringsArr = []
    for string in array2:
        for substring in array1:
            if substring in string:
                substringsArr.append(substring)
    return substringsArr



if __name__ == "__main__":
    a1 = ["live", "arp", "strong"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    r = ["arp", "live", "strong"]
    print("Answer", in_array(a1, a2))
