def find_even_index(arr):
    left_side = lambda i: sum(arr[:i])
    right_side = lambda i: sum(arr[i:])
    return [i for i, val in enumerate(arr) if left_side(i) == right_side(i)][0]

if __name__ == "__main__":
    even_index = find_even_index([1,2,3,2,1])
