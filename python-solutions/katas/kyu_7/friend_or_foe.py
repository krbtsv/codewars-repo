def friend(x: list[str]) -> list[str]:
    return [friend for friend in x if len(friend) == 4]
