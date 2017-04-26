def swap_elements(target_list, i_one, i_two):
    target_list[i_one], target_list[i_two] = target_list[i_two], target_list[i_one]
    return target_list

def next_bigger(n):
    int_list = [int(x) for x in str(n)]

    for ind, el in enumerate(int_list):
        ind_plus = ind 
        swapped_list = swap_elements(int_list, -ind_plus, -ind_plus - 1)
        num = int(''.join(map(str, swapped_list)))
        if (n < num):
            break

    # if (n < num):
    #     return swapped
    # else:
    #     swap_elements(int_list, )
    # return n < num

if __name__ == "__main__":
    answer = next_bigger(12345)
    print("Me Answer e", answer)
