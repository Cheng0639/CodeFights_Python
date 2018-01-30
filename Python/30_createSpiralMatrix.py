def createSpiralMatrix(n):
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    curDir = 0
    curPos = (n - 1, n - 1)
    res = [[0] * n for i in range(0,n)] 

    for i in range(1, n * n + 1):
        res[curPos[0]][curPos[1]] = i
        nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
        if not (0 <= nextPos[0] < n and
                0 <= nextPos[1] < n and
                res[nextPos[0]][nextPos[1]] == 0):
            curDir = (curDir + 1) % 4
            nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
        curPos = nextPos

    return res


print(createSpiralMatrix(3) == [[5, 4, 3],
                                [6, 9, 2],
                                [7, 8, 1]])
print(createSpiralMatrix(5) == [[9, 8, 7, 6, 5],
                                [10, 21, 20, 19, 4],
                                [11, 22, 25, 18, 3],
                                [12, 23, 24, 17, 2],
                                [13, 14, 15, 16, 1]])
