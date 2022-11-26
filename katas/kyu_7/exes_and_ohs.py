def xo(s):
    counter = {'x': 0, 'o': 0}
    for char in s.lower():
        if char in 'xo':
            counter[char] += 1
    return True if counter['x'] == counter['o'] else False


def xo_second_solution(s):
    from collections import Counter

    count = Counter(s.lower())
    return count.get('x', 0) == count.get('o', 0)
