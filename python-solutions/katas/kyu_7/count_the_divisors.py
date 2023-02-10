def divisors(n: int) -> int:
    return len([divisor for divisor in range(1, n + 1) if n % divisor == 0])
