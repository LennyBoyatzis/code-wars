from collections import Counter

def main():
    counter = Counter('superfluous')
    print("counter", counter)

    print(list(counter.elements()))
    print(list(counter.most_common(2)))

if __name__ == "__main__":
    print("Running the example...")
    main()

