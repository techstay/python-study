FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
OTHER_TENS = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
HUNDRED = "hundred"
THOUSAND = "thousand"


def tell_number(number):
    if number == 0:
        return "zero"
    elif number < 0:
        return "minus " + tell_number(-number)
    elif number < 10:
        return FIRST_TEN[number - 1]
    elif number < 20:
        return SECOND_TEN[number - 10]
    elif number < 100:
        a = number // 10
        b = number % 10
        if b == 0:
            return OTHER_TENS[a - 2]
        else:
            return OTHER_TENS[a - 2] + " " + tell_number(b)
    elif number < 1000:
        a = number // 100
        b = number % 100
        if b == 0:
            return tell_number(a) + " " + HUNDRED
        else:
            return tell_number(a) + " " + HUNDRED + " " + tell_number(b)
    else:
        a = number // 1000
        b = number % 1000
        if b == 0:
            return tell_number(a) + " " + THOUSAND
        else:
            return tell_number(a) + " " + THOUSAND + " " + tell_number(b)


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank 1
    assert tell_number(4) == "four", "1st example"
    assert tell_number(133) == "one hundred thirty three", "2nd example"
    assert tell_number(12) == "twelve", "3rd example"
    assert tell_number(101) == "one hundred one", "4th example"
    assert tell_number(212) == "two hundred twelve", "5th example"
    assert tell_number(40) == "forty", "6th example"
    assert not tell_number(212).endswith(
        " "
    ), "Dont forget strip whitespaces at the end of string"

    # Rank 2
    assert tell_number(-133) == "minus one hundred thirty three", "Minus"
    assert tell_number(0) == "zero", "Zero"

    # Rank 3
    assert tell_number(42000) == "forty two thousand", "42 many"
    assert (
        tell_number(-999999)
        == "minus nine hundred ninety nine thousand nine hundred ninety nine"
    ), "Abyss"

    print("Earn cool rewards by using the 'Check' button!")
