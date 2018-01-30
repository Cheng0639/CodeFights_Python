def calcBonuses(bonuses, n):
    it = iter(bonuses)
    res = 0

    try:
        for _ in range(n):
            res += next(it)
    except StopIteration:
        res = 0

    return res


print(calcBonuses([4, 2, 4, 5], 3) == 10)
print(calcBonuses([4, 2, 4, 5], 5) == 0)
print(calcBonuses([], 5) == 0)
print(calcBonuses([5, 3, 1, 9], 4) == 18)
print(calcBonuses([8, 8, 39, 33, 29, 35], 4) == 88)
