def friend(x: list[str]) -> list[str]:
    return [friend for friend in x if len(friend) == 4]


def friend_second_solution(x: list[str]) -> list[str]:
    import re

    true_friends = []
    for name in x:
        if len(name) == 4 and re.search('[a-zA-Z]', name):
            true_friends.append(name)
    return true_friends
