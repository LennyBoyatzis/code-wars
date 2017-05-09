is_odd = lambda i: i % 2 != 0

def sort_array(source_array):
    if not source_array:
        return []

    odd_list = []
    even_dict = {}

    for i, val in enumerate(source_array):
        if is_odd(val) and not 0:
            odd_list.append(val)
        else:
            even_dict[i] = val

    sorted_list = sorted(odd_list)

    for key, val in even_dict.items():
        print("key, val", key, val)
        sorted_list.insert(key, val)

    return sorted_list

if __name__ == "__main__":
    print(sort_array([0,1,2,3,4,5,6,7,8,9]))
