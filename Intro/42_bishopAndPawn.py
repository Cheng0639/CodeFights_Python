def bishopAndPawn(bishop, pawn):
    b = [ord(bishop[0]), int(bishop[1])]
    p = [ord(pawn[0]), int(pawn[1])]

    return abs((b[0] - p[0]) / (b[1] - p[1])) == 1


print(bishopAndPawn("a1", "c3") == True)
print(bishopAndPawn("h1", "h3") == False)
print(bishopAndPawn("e7", "a3") == True)
print(bishopAndPawn("e3", "a7") == True)
