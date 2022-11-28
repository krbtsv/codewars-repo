def get_middle(s):
    if len(s) == 1:
        return s
    elif len(s) % 2 != 0:
        return s[len(s) // 2:-(len(s) // 2)]
    elif len(s) % 2 == 0:
        return s[int(len(s) / 2 - 1):int((len(s) / 2 + 1))]
