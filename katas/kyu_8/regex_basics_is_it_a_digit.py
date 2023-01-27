def is_digit(n: str) -> bool:
    import re

    return bool(re.fullmatch(r'\d', n))


def is_digit_second_solution(n: str) -> bool:
    return n.isdigit() and len(n) == 1
