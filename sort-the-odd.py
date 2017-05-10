is_odd = lambda i: i % 2 != 0
is_even = lambda i: i % 2 == 0

def sort_array(arr):
    odd = sorted((i for i in arr if is_odd(i)), reverse=True)
    return [i if is_even(i) else odd.pop() for i in arr]

if __name__ == "__main__":
    print(sort_array([0,1,2,3,4,5,6,7,8,9]))
