def comp(array1, array2):
    try:
        return sorted([el * el for el in array1]) == sorted(array2)
    except:
        return False
