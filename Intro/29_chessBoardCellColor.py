def chessBoardCellColor(cell1, cell2):
    def slope(x, y):
        return ((ord(x) - ord('A') + 1) + (ord(y) - ord('1') + 1)) % 2 == 0

    return slope(cell1[0], cell1[1]) == slope(cell2[0], cell2[1])


print(chessBoardCellColor("A1", "C3") == True)
print(chessBoardCellColor("D2", "D2") == True)
print(chessBoardCellColor("A2", "A5") == False)
print(chessBoardCellColor("C8", "H8") == False)
print(chessBoardCellColor("G5", "E7") == True)
