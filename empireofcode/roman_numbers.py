def roman(number):
    def to_roman(n, A, B, C):
        if n <= 3:
            return A * n
        elif n <= 5:
            return A * (5 - n) + B
        elif n <= 8:
            return B + A * (n - 5)
        elif n <= 10:
            return A * (10 - n) + C

    def thousand_digit_to_roman(n):
        """Suppose n less than 4"""
        return "M" * n

    if number <= 10:
        return to_roman(number, "I", "V", "X")
    elif number <= 100:
        a = number // 10
        b = number % 10
        return to_roman(a, "X", "L", "C") + roman(b)
    elif number <= 1000:
        a = number // 100
        b = number % 100
        return to_roman(a, "C", "D", "M") + roman(b)
    elif number < 4000:
        a = number // 1000
        b = number % 1000
        return thousand_digit_to_roman(a) + roman(b)


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert roman(6) == "VI", "6"
    assert roman(76) == "LXXVI", "76"
    assert roman(499) == "CDXCIX", "499"
    assert roman(3888) == "MMMDCCCLXXXVIII", "3888"
    print("Earn cool rewards by using the 'Check' button!")
