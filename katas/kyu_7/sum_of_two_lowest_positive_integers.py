def quicksort(arr: list[int]) -> list:
    if len(arr) < 2:  # Базовый случай рекурсии
        return arr
    else:
        pivot = arr[0]  # Выбираем опорный элемент
        less = [el for el in arr if el < pivot]  # Подмассив всех элементов, меньших опорного
        greater = [el for el in arr if el > pivot]  # Подмассив всех элементов, больших опорного
        return quicksort(less) + [pivot] + quicksort(greater)


def sum_of_two_smallest_numbers(numbers: list[int]) -> int:
    sorted_numbers = quicksort(numbers)
    return sum(sorted_numbers[:2])
