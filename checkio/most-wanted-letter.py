def checkio(text):
    d = {}
    lower = [c for c in text.lower() if c.isalpha()]
    for c in lower:
        if c not in d:
            d.setdefault(c, 1)
        else:
            d[c] += 1
    from operator import itemgetter
    items = sorted(d.items(), key=itemgetter(0))
    items = sorted(items, key=itemgetter(1), reverse=True)
    return items[0][0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
