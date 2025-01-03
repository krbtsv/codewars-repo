# Complete the function that returns an array of length n, starting with the given number x and the squares of the previous number.
# If n is negative or zero, return an empty array/list.

# Examples
#
# 2, 5  -->  [2, 4, 16, 256, 65536]
# 3, 3  -->  [3, 9, 81]


def squares(x, n):
    if n <= 0:
        return []
    resultArr = []
    for i in range(n):
        if i > 0:
            x = pow(x, 2)
        resultArr.append(x)
    return resultArr


def squares2(x, n):
    return [x**(2**i) for i in range(n)]


def squares3(x: int, n: int) -> int:
    res = []
    for _ in range(n):
        res.append(x)
        x *= x
    return res