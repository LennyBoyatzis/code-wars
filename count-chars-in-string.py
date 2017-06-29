from collections import Counter
def count(string):
    return dict(Counter(string))


if __name__ == "__main__":
    print(count("Hello world"))
    print(count(""))
    print("Hello")
