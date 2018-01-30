def calkinWilfSequence(number):
    def fractions():
        n = 1
        d = 1
        yield [n, d]
        while True:
            n, d = d, 2 * (n // d) * d + d - n
            yield [n, d]

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res


print(calkinWilfSequence([1, 3]) == 3)
print(calkinWilfSequence([1, 1]) == 0)
print(calkinWilfSequence([3, 1]) == 6)
print(calkinWilfSequence([14, 3]) == 110)
print(calkinWilfSequence([7, 13]) == 129)
