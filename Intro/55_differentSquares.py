def differentSquares(matrix):
    return len(set(["".join([str(matrix[i + x][j + y]) for x in range(2) for y in range(2)]) for i in range(len(matrix) - 1) for j in range(len(matrix[i]) - 1)]))


print(differentSquares([[1, 2, 1],
                        [2, 2, 2],
                        [2, 2, 2],
                        [1, 2, 3],
                        [2, 2, 1]]) == 6)
print(differentSquares([[9, 9, 9, 9, 9],
                        [9, 9, 9, 9, 9],
                        [9, 9, 9, 9, 9],
                        [9, 9, 9, 9, 9],
                        [9, 9, 9, 9, 9],
                        [9, 9, 9, 9, 9]]) == 1)
print(differentSquares([[3]]) == 0)
print(differentSquares([[3],
                        [4],
                        [5],
                        [6],
                        [7]]) == 0)
print(differentSquares([[2, 5, 3, 4, 3, 1, 3, 2],
                        [4, 5, 4, 1, 2, 4, 1, 3],
                        [1, 1, 2, 1, 4, 1, 1, 5],
                        [1, 3, 4, 2, 3, 4, 2, 4],
                        [1, 5, 5, 2, 1, 3, 1, 1],
                        [1, 2, 3, 3, 5, 1, 2, 4],
                        [3, 1, 4, 4, 4, 1, 5, 5],
                        [5, 1, 3, 3, 1, 5, 3, 5],
                        [5, 4, 4, 3, 5, 4, 4, 4]]) == 54)
print(differentSquares(
    [[1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 9, 9, 9, 2, 3, 9]]) == 0)
