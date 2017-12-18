def golf(n, r=1):
    """Indent only one space would get 3 stars"""
    for i in str(n):
        r *= max(int(i), 1)
    return r


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert golf(123405) == 120
    assert golf(999) == 729
    assert golf(1000) == 1
    assert golf(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
