def find_short(s):
    return sorted([len(length) for length in s.split()])[0]
