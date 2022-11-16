def accum(s):
    return '-'.join([(s[i] * (i + 1)).capitalize() for i in range(len(s))])


def accum_second_solution(s):
    return '-'.join([letter.upper() + letter.lower() * index for index, letter in enumerate(s)])
