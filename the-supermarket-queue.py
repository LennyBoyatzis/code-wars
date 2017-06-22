def queue_time(customers, n):
    if not customers:
        return 0

    if n == 1:
        return sum(customers)

    queues=[0]*n
    for checkout_time in customers:
        # O(n log n)
        queues.sort()
        # Add next customers time 
        # to the next available checkout
        queues[0] += checkout_time
    return max(queues)


if __name__ == "__main__":
    customers = [2,3,10];
    customers = [2,3,5,2,1,6];
    print(queue_time(customers, 3))
