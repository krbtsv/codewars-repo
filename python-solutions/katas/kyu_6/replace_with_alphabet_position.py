def alphabet_position(text):
    alphabet = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
        'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
        'x': 24, 'y': 25, 'z': 26
    }
    return ' '.join([str(alphabet[letter.lower()]) for letter in text if letter.isalpha()])


def alphabet_position_second_solution(text):
    from string import ascii_lowercase
    return ' '.join(str(ascii_lowercase.index(letter.lower()) + 1) for letter in text if letter.isalpha())
