def fixResult(result):
    def fix(x):
        return x // 10

    return list(map(fix, result))


print(fixResult([42, 239, 365, 50]) == [4, 23, 36, 5])
print(fixResult([42, 239, 365, 50]) == [4, 23, 36, 5])
print(fixResult([]) == [])
print(fixResult([31, 41, 59, 26, 53, 58, 97, 93]) == [3, 4, 5, 2, 5, 5, 9, 9])
