def capitals(word):
    return [word.index(letter, index) for index, letter in enumerate(word) if letter.isupper()]

if __name__ == "__main__":
    print(capitals("CodEWaRs"))
