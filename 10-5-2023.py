def min_task_cost(arr):
    arr.sort()
    n = len(arr)
    min_cost = float('inf')
    for i in range(n):
        excluded_worker = arr[i]
        remaining_workers = arr[:i] + arr[i+1:]
        pairs = [(remaining_workers[j], remaining_workers[j+1]) for j in range(0, n-2, 2)]
        cost = sum(abs(a-b) for a, b in pairs)
        if cost < min_cost:
            excluded_worker_min = excluded_worker
            min_cost = cost
    return min_cost


arr = [1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111, 123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]
min_cost = min_task_cost(arr)
print("The minimum cost is", min_cost)

