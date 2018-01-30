def minesweeper(matrix):
    return[
        [
            sum([matrix[i + a][j + b]
                 for a in range((0 if i == 0 else -1), (1 if i == len(matrix) - 1 else 2))
                 for b in range((0 if j == 0 else -1), (1 if j == len(matrix[i]) - 1 else 2))
                 ]
                )
            - (1 if matrix[i][j] else 0)
            for j in range(0, len(matrix[i]))
        ]
        for i in range(0, len(matrix))]


print(minesweeper([[True, False, False],
                   [False, True, False],
                   [False, False, False]]) == [[1, 2, 1],
                                               [2, 1, 1],
                                               [1, 1, 1]])
print(minesweeper([[False, False, False],
                   [False, False, False]]) == [[0, 0, 0],
                                               [0, 0, 0]])
print(minesweeper([[True, False, False, True],
                   [False, False, True, False],
                   [True, True, False, True]]) == [[0, 2, 2, 1],
                                                   [3, 4, 3, 3],
                                                   [1, 2, 3, 1]])
