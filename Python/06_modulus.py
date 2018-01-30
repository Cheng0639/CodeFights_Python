def modulus(n):
    if n % 1 == 0:
        return n % 2
    else:
        return -1


print(modulus(15) == 1)
print(modulus(23.12) == -1)
print(modulus(0) == 0)
print(modulus(232.2423) == -1)
print(modulus(30) == 0)
print(modulus(11) == 1)
