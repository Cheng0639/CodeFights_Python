def spiralNumbers(n):
    rlt = [[0 for i in range(1, n + 1)] for i in range(n)]
    x = 0
    y = 0
    dx = 0
    dy = 1
    for cnt in range(1, n**2 + 1):
        rlt[x][y] = cnt

        if (dx == 1):
            if (x == n - 1 or rlt[x + 1][y] != 0):
                dx = 0
                dy = -1
        elif(dx == -1):
            if (x == 0 or rlt[x - 1][y] != 0):
                dx = 0
                dy = 1
        elif(dy == 1):
            if (y == n - 1 or rlt[x][y + 1] != 0):
                dx = 1
                dy = 0
        elif(dy == -1):
            if (y == 0 or rlt[x][y - 1] != 0):
                dx = -1
                dy = 0

        x += dx
        y += dy
        cnt += 1
    return rlt


print(spiralNumbers(3) == [[1, 2, 3],
                           [8, 9, 4],
                           [7, 6, 5]])
print(spiralNumbers(5) == [[1, 2, 3, 4, 5],
                           [16, 17, 18, 19, 6],
                           [15, 24, 25, 20, 7],
                           [14, 23, 22, 21, 8],
                           [13, 12, 11, 10, 9]])
