from fractions import gcd
from functools import reduce


def leastCommonDenominator(denominators):
    return reduce(lambda ori, new: (ori * new) / gcd(ori, new), denominators)


print(gcd(4, 12))
print(leastCommonDenominator([2, 3, 4, 5, 6]) == 60)
print(leastCommonDenominator([34, 6, 3, 5, 3]) == 510)
