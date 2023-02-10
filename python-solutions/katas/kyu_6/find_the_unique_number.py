from collections import Counter


def find_uniq(arr):
    counts = Counter(arr)
    return sorted(counts.items(), key=lambda x: x[1])[0][0]


def find_uniq_second_solution(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
