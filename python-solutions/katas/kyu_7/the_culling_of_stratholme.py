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
def purify(s: str) -> str:
    from re import sub

    return " ".join(word for word in sub(r"(?i)\w?i+\w?", "", s).split())


@test_time
def purify_second_solution(s: str) -> str:
    import re

    return ' '.join(re.sub(r'[\S]?[iI][^\siI]?', '', s).split())


string = "zippity duppity bopity bip ZIPPITY DUPPITY BOPITY BIP"
for func in [purify, purify_second_solution]:
    func(string)
