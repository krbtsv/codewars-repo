def get_union_set_letters(s1: str, s2: str) -> set:
    letters_lst1 = [char for char in s1 if char.isalpha() and char.isupper() is False]
    letters_lst2 = [char for char in s2 if char.isalpha() and char.isupper() is False]
    letters_set1 = set(letters_lst1)
    letters_set2 = set(letters_lst2)
    union_set1_set2 = letters_set1.union(letters_set2)

    return union_set1_set2


def mix(s1: str, s2: str) -> str:
    union_sets = get_union_set_letters(s1, s2)
    result_lst = []
    for letter in union_sets:
        if s1.count(letter) > 1 or s2.count(letter) > 1:
            if s1.count(letter) > s2.count(letter):
                result_lst.append(f'1:{letter * s1.count(letter)}')
            elif s1.count(letter) < s2.count(letter):
                result_lst.append(f'2:{letter * s2.count(letter)}')
            elif s1.count(letter) == s2.count(letter):
                result_lst.append(f'=:{letter * s1.count(letter)}')
    result_lst.sort()
    result_lst.sort(key=len, reverse=True)
    return '/'.join(result_lst)


def mix_second_solution(s1: str, s2: str) -> str:
    import string

    result = []

    for i in string.ascii_lowercase:
        more = max(s1.count(i), s2.count(i))
        get_prefix = lambda x: '=:' if x == s1.count(i) == s2.count(i) else ('1:' if x == s1.count(i) else '2:')
        if more > 1:
            result.append(get_prefix(more) + i * more)

    return '/'.join(sorted(result, key=lambda x: (-len(x), ascii(x))))
