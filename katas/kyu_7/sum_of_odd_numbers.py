def row_sum_odd_numbers(n):
    start = (n * n) - (n - 1)
    end = start + n * 2
    return sum(i for i in range(start, end, 2))
