def primesSum(a, b):
    return sum(map(lambda x: 0 if x < 2 or any([x % i == 0 for i in range(2, int(x ** 0.5) + 1)]) else x, range(a, b + 1)))


def primesSum1(a, b):
    return sum([i for i in range(a, b + 1) if not(i < 2 or any(i % j == 0 for j in range(2, int(i**0.5) + 1)))])


def primesSum2(a, b):
    return sum(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)), range(max(2, a), b + 1)))


print(primesSum(10, 20) == 60)
print(primesSum(1, 7) == 17)
print(primesSum(24, 28) == 0)
print(primesSum(13, 13) == 13)
