def multiplicationTable(n):
    return [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]


print(multiplicationTable(5))
