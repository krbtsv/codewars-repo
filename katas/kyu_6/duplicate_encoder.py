from collections import Counter


def duplicate_encode(word):
    counts = Counter(word.lower())
    return ''.join('(' if counts[v] == 1 else ')' for v in word)
