def test_time(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Time result is {end_time - start_time}')
        return result

    return wrapper


@test_time
def string_clean(s: str) -> str:
    import re

    return ''.join(re.findall(r'\D', s))


@test_time
def string_clean_second_solution(s: str) -> str:
    import re

    return re.sub(r'\d', '', s)


@test_time
def string_clean_third_solution(s: str) -> str:
    return ''.join(x for x in s if not x.isdigit())


@test_time
def string_clean_fourth_solution(s: str) -> str:
    for d in '0123456789':
        s = s.replace(d, '')
    return s


string = '33333Ad2dsad3ds21 A3333  1$$s122a!d! A2!A!3Ae$24 f2##222 '
for func in [string_clean, string_clean_second_solution, string_clean_third_solution, string_clean_fourth_solution]:
    print(func(string), end='\n\n')
