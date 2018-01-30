def calcFinalScore(scores, n):
    gen = map(lambda x: pow(x, 2), sorted(scores, reverse=True))

    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res //= 5

    return res


print(calcFinalScore([4, 2, 4, 5], 3) == 57)
print(calcFinalScore([4, 2, 4, 5], 5) == 12)
print(calcFinalScore([], 5) == 0)
print(calcFinalScore([5, 3, 1, 9], 4) == 116)
print(calcFinalScore([3, 9, 0, 50], 1) == 2500)
