def constructShell(n):
    return [[0] * i for i in range(1, n + 1)] + [[0] * i for i in range(n - 1, 0, -1)]


print(constructShell(3) == [[0],
                            [0, 0],
                            [0, 0, 0],
                            [0, 0],
                            [0]])
print(constructShell(5) == [[0],
                            [0, 0],
                            [0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0],
                            [0, 0],
                            [0]])
