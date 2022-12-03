def take_and_split(i: int) -> int:
    return sum([int(d) for d in str(i)])


def power_sum_dig_term(n):
    res = []

    for i in range(2, 200):
        for j in range(2, 20):
            raised_num = pow(i, j)
            if take_and_split(raised_num) == i:
                res.append(raised_num)
    return sorted(res)[n - 1]
