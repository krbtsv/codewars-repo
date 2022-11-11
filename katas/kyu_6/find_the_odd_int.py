def find_it(seq):
    num_counter = {}
    for num in seq:
        num_counter[num] = num_counter.get(num, 0) + 1
    for el in num_counter:
        if num_counter[el] % 2 != 0:
            return el
