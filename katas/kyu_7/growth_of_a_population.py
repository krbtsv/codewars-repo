def nb_year(p0, percent, aug, p):
    counter = 0
    while p0 < p:
        p0 += int(p0 * (percent / 100) + aug)
        counter += 1
    return counter


def nb_year_second_solution(p0, percent, aug, p, count=0):
    if p0 >= p:
        return count
    else:
        count += 1
        pop = int(p0 + p0 * (percent / 100) + aug)
        return nb_year_second_solution(pop, percent, aug, p, count)
