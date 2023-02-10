from collections import Counter


def anagrams(word, words):
    return [wd for wd in words if sorted(word) == sorted(wd)]


def anagrams_second_solution(word, words):
    return [wd for wd in words if Counter(word) == Counter(wd)]
