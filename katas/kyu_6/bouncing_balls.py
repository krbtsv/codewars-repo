def bouncing_ball(h: float, bounce: float, window: float) -> int:
    if not (h > 0 and 0 < bounce < 1 and window < h):
        return -1
    else:
        res = h * bounce
        count = 1
        while res > window:
            res *= bounce
            count += 2
        return count


def bouncing_ball_second_solution(h: float, bounce: float, window: float) -> int:
    if not (h > 0 and 0 < bounce < 1 and window < h):
        return -1
    return 2 + bouncing_ball_second_solution(h * bounce, bounce, window)
