def calc_time(customers, tellers):
    if tellers == 1:
        return sum(customers)

    being_served = customers[:tellers]
    waiting_line = customers[tellers:]

    for customer in waiting_line:
       being_served.sort()
       being_served[0] += customer

    return max(being_served)


if __name__ == "__main__":
    print(calc_time([5,3,4], 1))
    print(calc_time([10,2,3,3], 2))
    print(calc_time([2,3,10], 2))
