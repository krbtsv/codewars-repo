def get_blast_indexes(airstrikes: str, battlefield_size: int) -> list:
    indexes = []
    for i, strike in enumerate(airstrikes):
        if strike == '*':
            indexes += [i - 1, i, i + 1]
    return list(filter(lambda x: x >= 0 and x < battlefield_size, set(indexes)))


def alphabet_war(reinforces: list[str], airstrikes: list[str]) -> str:
    battlefield_size = len(reinforces[0])

    # SETUP BATTLEFIELD (LAYER SOLDIERS)
    battlefield = [[] for x in range(battlefield_size)]
    for row, layer in enumerate(reinforces):
        for col, letter in enumerate(layer):
            battlefield[col].append(letter)

    # FIND INDEXES OF EACH AIRSTRIKE AND REMOVE SOLDIER FROM POSITION
    for airstrike in airstrikes:
        indexes = get_blast_indexes(airstrike, battlefield_size)
        for index in indexes:
            if battlefield[index] == ['_']:
                continue
            elif len(battlefield[index]) == 1:
                battlefield[index] = ['_']
            else:
                battlefield[index].pop(0)
    return ''.join(list(map(lambda x: x[0], battlefield)))


print(alphabet_war(["abcdefg", "hijklmn"], ["   *   ", "*  *   "]))
