def solution(args):
    lst_chain = []
    lst_result = []
    for num in sorted(args) + [None]:
        if not lst_chain:
            lst_chain.append(num)
        else:
            if num == lst_chain[-1] + 1:
                lst_chain.append(num)
            else:
                if len(lst_chain) > 2:
                    lst_result.append(str(lst_chain[0]) + '-' + str(lst_chain[-1]))
                else:
                    lst_result.extend(str(x) for x in lst_chain)
                lst_chain = [num]
    return ','.join(lst_result)


print(solution([-4, -3, -2, -1, 0, 5, 6, 7]))
