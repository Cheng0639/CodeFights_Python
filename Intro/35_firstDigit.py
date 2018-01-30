def firstDigit(inputString):
    for i in inputString:
        if i.isdigit():
            return i


print(firstDigit("var_1__Int") == '1')
print(firstDigit("q2q-q") == '2')
print(firstDigit("0ss") == '0')
