def test_time(func):
    def wrapper(*args, **kwargs):
        from time import time
        start_time = time()
        res = func(*args, **kwargs)
        end_time = time()
        print(f'Time execution is {end_time - start_time}')
        return res

    return wrapper


@test_time
def encrypt_this(text: str) -> str:
    result = []
    lst = text.split()
    for word in lst:
        if len(word) > 2:
            ascii_letter = str(ord(word[0]))
            word = ascii_letter + word[1:]
            word = ascii_letter + word[-1] + word[len(ascii_letter) + 1: -1] + word[
                                                                               len(ascii_letter): len(ascii_letter) + 1]
            result.append(word)
        else:
            ascii_letter = str(ord(word[0]))
            word = ascii_letter + word[1:]
            result.append(word)

    return ' '.join(result)


@test_time
def encrypt_this_second_solution(text: str) -> str:  # Stylishly solution
    result = []

    for word in text.split():
        # turn word into a list
        word = list(word)

        # replace first letter with ascii code
        word[0] = str(ord(word[0]))

        # switch 2nd and last letters
        if len(word) > 2:
            word[1], word[-1] = word[-1], word[1]

        # add to results
        result.append(''.join(word))

    return ' '.join(result)


strings = [
    "A wise old owl lived in an oak",
    "The more he saw the less he spoke",
    "The less he spoke the more he heard",
    "Why can we not all be like that wise old bird"
    "Thank you Piotr for all your help"
]

for string in strings:
    for func in [encrypt_this, encrypt_this_second_solution]:
        print(func(string))
    print('\nNext test')
