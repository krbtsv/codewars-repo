def get_true_string(fight: str) -> str:
    SWAP = {'j': {'w': 'm', 'p': 'q', 'b': 'd', 's': 'z'}, 't': {'m': 'w', 'q': 'p', 'd': 'b', 'z': 's'}}

    lst = [fight[-1]]
    for i in range(len(fight) - 1):
        if fight[i + 1] in 'tj' and i + 1 < len(fight) - 1:
            lst.append(SWAP[fight[i + 1]].get(fight[i]))
        elif fight[i - 1] in 'tj' and 0 < i - 1 < len(fight):
            lst.append(SWAP[fight[i - 1]].get(fight[i]))
        else:
            lst.append(fight[i])

    return ''.join(lst)


def alphabet_war(fight: str) -> str:
    costs = {'left': {'w': 4, 'p': 3, 'b': 2, 's': 1}, 'right': {'m': 4, 'q': 3, 'd': 2, 'z': 1}}
    left_side_counter = 0
    right_side_counter = 0

    fight = get_true_string(fight)

    for letter in fight:
        if costs['left'].get(letter):
            left_side_counter += costs['left'][letter]
        elif costs['right'].get(letter):
            right_side_counter += costs['right'][letter]
        else:
            continue

    return {True: "Left side wins!", False: "Right side wins!"}[
        right_side_counter < left_side_counter] if left_side_counter != right_side_counter else "Let's fight again!"
