def tribonacci(signature: list, n: int) -> list:
    if len(signature) > n:
        return signature[:n]
    shift = 0
    for i in range(3, n):
        signature.append(sum(signature[shift:i]))
        shift += 1
    return signature


def tribonacci_second_solution(signature: list, n: int) -> list:
    return signature[:n] if n <= len(signature) else tribonacci_second_solution(signature + [sum(signature[-3:])], n)
