def binary_array_to_number(arr):
    return sum(digit * pow(2, i) for i, digit in enumerate(reversed(arr)))
