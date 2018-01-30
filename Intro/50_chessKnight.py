def chessKnight(cell):
    x, y = ord(cell[0]) - 96, int(cell[1])
    return sum([1 <= x + i <= 8 and 1 <= y + j <= 8 for i in [1, 2, -2, -1]
                for j in [1, 2, -2, -1] if abs(i) != abs(j)])


print(chessKnight("a1") == 2)
print(chessKnight("c2") == 6)
print(chessKnight("d4") == 8)
print(chessKnight("g6") == 6)
