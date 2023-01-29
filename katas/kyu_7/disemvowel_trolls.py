def test_time(func):
    def wrapper(*args, **kwargs):
        from time import time
        start_time = time()
        res = func(*args, **kwargs)
        end_time = time()
        print(f'Time result is {end_time - start_time}')
        return res

    return wrapper


@test_time
def disemvowel(string_: str) -> str:
    import re

    return ''.join(re.findall(r'[^aeoiu]', string_, re.I))


@test_time
def disemvowel_second_solution(string_: str) -> str:
    return ''.join(letter for letter in string_ if letter.lower() not in 'aeoiu')


@test_time
def disemvowel_third_solution(string_: str) -> str:
    for i in "aeiouAEIOU":
        string_ = string_.replace(i, '')
    return string_


string = "This website is for losers LOL!"
for func in [disemvowel, disemvowel_second_solution, disemvowel_third_solution]:
    print(func(string))
