def descending_order(num):
    return int(''.join(sorted([digit for digit in str(num)], reverse=True)))
