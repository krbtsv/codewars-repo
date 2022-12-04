opposite_side = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}


def dir_reduc(arr):
    res_path = []
    for side in arr:
        if res_path and opposite_side[side] == res_path[-1]:
            res_path.pop()
        else:
            res_path.append(side)
    return res_path


opposites = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]


def dir_resuc_second_solution(arr):
    for i in range(len(arr) - 1):
        if set(arr[i:i + 2]) in opposites:
            del arr[i:i + 2]
            return dir_resuc_second_solution(arr)
    return arr
