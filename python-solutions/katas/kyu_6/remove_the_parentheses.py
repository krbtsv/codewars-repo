import re
import time


def test_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f'Time execution is {end_time - start_time}')
        return res

    return wrapper


@test_time
def remove_parentheses(s: str) -> str:
    while '(' in s:
        s = re.sub("\([^()]*\)", "", s)
    return s


@test_time
def remove_parentheses_second_solution(s: str) -> str:
    while re.findall(r"\([^()]*\)", s):
        s = re.sub(r"\([^()]*\)", "", s)
    return s


@test_time
def remove_parentheses_third_solution(s: str) -> str:
    res, count = "", 0
    for letter in s:
        if letter == "(":
            count += 1
        elif letter == ")":
            count -= 1
        elif count == 0:
            res += letter
    return res


string = "hello example (words(more words) here) something"
for func in [remove_parentheses, remove_parentheses_second_solution, remove_parentheses_third_solution]:
    print(func(string))
