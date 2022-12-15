def solve(money: int, coins: list[int], length: int) -> int:
    """
    :param money:
    :param coins:
    :param length:
    :return: count of change combinations for money
    """

    if length < 0 or money < 0:
        return 0
    if money == 0:
        return 1

    count = solve(money, coins, length - 1) + solve(money - coins[length], coins, length)

    return count


def count_change(money: int, coins: list[int]) -> int:
    return solve(money, coins, len(coins) - 1)


def count_change_second_solution(money: int, coins: list[int]) -> int:
    count = [0] * (money + 1)  # counts number of possibilties
    count[0] = 1
    for i in range(len(coins)):
        j = coins[i]
        while j <= money:
            count[j] += count[j - coins[i]]
            j += 1
    return count[money]


# It's not my solution ((( XD
