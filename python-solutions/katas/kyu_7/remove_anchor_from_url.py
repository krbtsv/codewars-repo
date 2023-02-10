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
def remove_url_anchor(url: str) -> str:
    import re

    return ''.join(re.sub(r'[#]\w+', '', url))


@test_time
def remove_url_anchor_second_solution(url: str) -> str:
    return url.split('#')[0]


string = "www.codewars.com#about"
for func in [remove_url_anchor, remove_url_anchor_second_solution]:
    print(func(string))
