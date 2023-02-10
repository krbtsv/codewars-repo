def decomp(n: int) -> str:
    import math

    n = math.factorial(n)
    res = []
    for i in range(2, n):
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count > 1:
            res.append(f'{i}^{count}')
        elif count == 1:
            res.append(f'{i}')
        if n == 1:
            break
    return ' * '.join(res)
