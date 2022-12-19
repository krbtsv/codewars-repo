def queue_time(customers: list[int], n: int) -> int:
    queues = [0 for i in range(n)]
    for customer_time in customers:
        queues[queues.index(min(queues))] += customer_time
    return max(queues)
