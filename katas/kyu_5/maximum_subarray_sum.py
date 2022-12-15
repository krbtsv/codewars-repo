def max_sequence_perfect_solution(array):  # O(n)
    iter_array = iter(array)
    try:
        temp_sum = next(iter_array)
    except StopIteration:
        temp_sum = 0
    max_sum = temp_sum
    for item in iter_array:
        temp_sum = max(temp_sum + item, item)
        max_sum = max(temp_sum, max_sum)
    return max(max_sum, 0)


def max_sequence_simple_fast_solution(arr):  # Not my, but very nice solution O(n)
    maximum, current_maximum = 0, 0
    for el in arr:
        current_maximum += el
        if current_maximum < 0:
            current_maximum = 0
        if current_maximum > maximum:
            maximum = current_maximum
    return maximum


def max_sequence(arr):  # My solution O(n^2)
    maximum = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if sum(arr[i:j + 1]) > maximum:
                maximum = sum(arr[i:j + 1])
    return maximum


def max_sequence_second_solution(arr):  # Another solution O(n^2)
    res_lst = []
    for index, value in enumerate(arr):
        res_lst.append(value)
        for i in range(index + 1, len(arr)):
            value += arr[i]
            res_lst.append(value)
    if all(i < 0 for i in arr) or not res_lst:
        return 0
    else:
        return max(res_lst)
