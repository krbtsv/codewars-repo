def move_zero(arr):
    if type(arr) != list:
        raise TypeError('Please enter a list!')
    return sorted(arr, key=lambda x: x == 0 and type(x) is not bool)
