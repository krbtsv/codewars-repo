def perfect_square(square: str) -> bool:
    square = square.split()
    for char in square:
        if len(char) != len(square) or len(char) != char.count('.'):
            return False
    return True
