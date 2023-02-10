def square_digits(num: int) -> int:
    return int(''.join([str(pow(int(digit), 2)) for digit in str(num)]))
