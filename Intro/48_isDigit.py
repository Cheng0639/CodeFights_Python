def isDigit(symbol):
    return str.isdigit(symbol)


print(isDigit("0") == True)
print(isDigit("-") == False)
print(isDigit("O") == False)
print(isDigit("1") == True)
print(isDigit("2") == True)
print(isDigit("!") == False)
print(isDigit("@") == False)
print(isDigit("+") == False)
