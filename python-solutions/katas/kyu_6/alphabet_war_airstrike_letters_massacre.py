def test_time(func):
    def wrapper(*args, **kwargs):
        from time import time
        start_time = time()
        res = func(*args, **kwargs)
        end_time = time()
        print(f"Time execution is {end_time - start_time}")
        return res

    return wrapper


@test_time
def alphabet_war(fight: str) -> str:
    import re

    fight = re.sub(r'.?[*]+.?', '', fight)
    costs = {'w': 4, 'p': 3, 'b': 2, 's': 1,
             'm': -4, 'q': -3, 'd': -2, 'z': -1}

    result = sum(costs[char] for char in fight if char in costs)

    return {
        result == 0: "Let's fight again!",
        result > 0: "Left side wins!",
        result < 0: "Right side wins!",
    }[True]


@test_time
def alphabet_war_second_solution(fight: str) -> str:
    import re

    powers = {
        'w': -4, 'p': -3, 'b': -2, 's': -1,
        'm': +4, 'q': +3, 'd': +2, 'z': +1,
    }
    fight = re.sub('.(?=\*)|(?<=\*).', '', fight)
    result = sum(powers.get(c, 0) for c in fight)
    if result < 0:
        return 'Left side wins!'
    elif result > 0:
        return 'Right side wins!'
    else:
        return "Let's fight again!"


string = "mb**qwwp**dm"
for func in [alphabet_war, alphabet_war_second_solution]:
    print(func(string))
