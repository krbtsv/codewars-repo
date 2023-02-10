def two_sum(numbers: list, target: int) -> list:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]


def two_sum_second_solution(numbers, target):
    compliments = {}
    for i in range(len(numbers)):
        if numbers[i] in compliments:
            return [compliments[numbers[i]], i]
        compliments[target - numbers[i]] = i
