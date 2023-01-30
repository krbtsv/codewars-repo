def test_time(func):
    def wrapper(*args, **kwargs):
        from time import time
        start_time = time()
        res = func(*args, **kwargs)
        end_time = time()
        print(f'Time execution is {end_time - start_time}')
        return res

    return wrapper


@test_time
def alphabet_war(fight: str) -> str:
    costs = {'left': {'w': 4, 'p': 3, 'b': 2, 's': 1}, 'right': {'m': 4, 'q': 3, 'd': 2, 'z': 1}}
    left_side_counter = 0
    right_side_counter = 0

    for letter in fight:
        if costs['left'].get(letter):
            left_side_counter += costs['left'][letter]
        elif costs['right'].get(letter):
            right_side_counter += costs['right'][letter]
        else:
            continue

    return {True: "Left side wins!", False: "Right side wins!"}[
        right_side_counter < left_side_counter] if left_side_counter != right_side_counter else "Let's fight again!"


@test_time
def alphabet_war_second_solution(fight: str) -> str:
    d = {'w': 4, 'p': 3, 'b': 2, 's': 1,
         'm': -4, 'q': -3, 'd': -2, 'z': -1}
    r = sum(d[c] for c in fight if c in d)

    return {r == 0: "Let's fight again!",
            r > 0: "Left side wins!",
            r < 0: "Right side wins!"
            }[True]


string = "zdqmwpbs"
for func in [alphabet_war, alphabet_war_second_solution]:
    print(func(string))
