def order(sentence):
    lst = sentence.split()
    array = []
    for word in lst:
        for char in word:
            if char.isdigit():
                array.append((char, word))
    array = sorted(array, key=lambda x: x[0])
    return ' '.join(i[1] for i in array)


def order_second_solution(words):
    return ' '.join(sorted(words.split(), key=lambda w: sorted(w)))
