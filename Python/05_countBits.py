def countBits(n):
    return n.bit_length()


print(countBits(50) == 6)
print(countBits(1) == 1)
print(countBits(1000000000) == 30)
print(countBits(237487384) == 28)
print(countBits(278) == 9)
