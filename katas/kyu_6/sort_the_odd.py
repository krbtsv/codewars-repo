def sort_array(source_array):
    for i in range(0, len(source_array)):
        for j in range(i, len(source_array)):
            if source_array[i] % 2 != 0 and source_array[j] % 2 != 0:
                if source_array[j] < source_array[i]:
                    source_array[j], source_array[i] = source_array[i], source_array[j]
    return source_array


def sort_array_second_solution(source_array):
    odds = sorted((x for x in source_array if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in source_array]
