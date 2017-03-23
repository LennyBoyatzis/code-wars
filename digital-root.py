def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

if __name__ == "__main__":
    print("Root --->", digital_root(154534))
