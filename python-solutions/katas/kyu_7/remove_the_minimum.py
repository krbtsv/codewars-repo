def find_smallest_index(arr: list[int]) -> int:  # O(n)
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def remove_smallest(numbers: list[int]) -> list[int]:  # O(1)
    numbers_copy = numbers[:]
    if numbers_copy:
        numbers_copy.pop(find_smallest_index(numbers_copy))
    return numbers_copy


def remove_smallest_second_solution(numbers: list[int]) -> list[int]:
    numbers_copy = numbers[:]
    if numbers_copy:
        numbers_copy.remove(min(numbers_copy))
    return numbers_copy
