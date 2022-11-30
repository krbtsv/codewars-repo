def expanded_form(num):
    num = str(num)
    result = []
    for index, digit in enumerate(num):
        if digit != '0':
            result.append(digit + '0' * len(num[index + 1:]))
    return ' + '.join(result)


def expanded_form_second_solution(num):
    return ' + '.join([d + '0' * i for i, d in enumerate(str(num)[::-1]) if d != '0'][::-1])
