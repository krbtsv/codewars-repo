def duplicate_count(text):
    text = text.lower()
    lst = [char for char in text if text.count(char) > 1]
    return len(set(lst))


def duplicate_count_second_solution(text):
    from collections import Counter

    return sum(1 for char, counts in Counter(text.lower()).items() if counts > 1)
