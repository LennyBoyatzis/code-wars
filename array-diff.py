def array_diff(a, b):
    return [ y for y in a if y not in b ]

if __name__ == "__main__":
    a = [1,2,3,4,4,4,4,5]
    b = [4,5]
    print(array_diff(a,b))
