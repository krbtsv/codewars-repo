def persistence(n):
    counter = 0
    while len(str(n)) != 1:
        lst = [digit for digit in str(n)]
        n = eval('*'.join(lst))
        counter += 1
    return counter


def persistence_second_solution(n, count=0):
    return count if n < 10 else persistence_second_solution(eval('*'.join(list(str(n)))), count + 1)
