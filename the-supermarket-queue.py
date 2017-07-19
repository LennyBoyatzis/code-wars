def queue_time(customers, tellers):
    teller_times = [0] * tellers

    for customer in customers:
        teller_times.sort()
        teller_times[0] += customer
    return max(teller_times)


if __name__ == "__main__":
    print(queue_time([10,2,3,3], 1)) # 18
    print(queue_time([10,2,3,3], 2)) # 10
    print(queue_time([2,3,10], 2)) # 12
