def is_it_a_num(s: str) -> str:
    import re

    searched_digits = re.findall('[0-9]', s)
    return ''.join(searched_digits) if (
            len(searched_digits) == 11 and searched_digits[0] == '0') else 'Not a phone number'


def is_it_a_num_second_solution(s: str) -> str:
    t = ''.join(i for i in s if i.isdigit())
    return t if len(t) == 11 and t[0] == "0" else 'Not a phone number'
