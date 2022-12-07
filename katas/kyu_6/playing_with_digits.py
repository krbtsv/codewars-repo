def dig_pow(n, p):
    digits = (int(i) for i in str(n))
    result = 0
    for x in digits:
        result += pow(x, p)
        p += 1
    if result % n:
        return -1
    else:
        return result // n


def dig_pow_second_solution(n, p):
    sequence_sum = 0
    for index, digit in enumerate(str(n)):
        sequence_sum += pow(int(digit), p + index)
    return -1 if sequence_sum % n else sequence_sum // n
