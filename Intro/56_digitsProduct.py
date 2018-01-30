def digitsProduct(product):
    if product == 0:
        return 10

    if product == 1:
        return 1

    rlt = ""

    for i in range(2, 10)[::-1]:
        while(product % i == 0):
            product /= i
            rlt += str(i)

    if(product > 1):
        return -1

    return int(rlt[::-1])


print(digitsProduct(12) == 26)
print(digitsProduct(19) == -1)
print(digitsProduct(450) == 2559)
print(digitsProduct(0) == 10)
print(digitsProduct(13) == -1)
print(digitsProduct(1) == 1)
print(digitsProduct(243) == 399)
print(digitsProduct(576) == 889)
print(digitsProduct(360) == 589)
