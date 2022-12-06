def first_non_consecutive(arr):
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) != 1:
            return arr[i + 1]
    return None


def first_non_consecutive_second_solution(arr):
    return next((j for i, j in zip(arr, arr[1:]) if i + 1 != j), None)
