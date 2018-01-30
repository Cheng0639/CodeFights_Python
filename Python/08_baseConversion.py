def baseConversion(n, x):
    return "{0:x}".format(int(n, x))


print(baseConversion("1302", 5) == "ca")
print(baseConversion("1010100101", 2) == "2a5")
print(baseConversion("30", 4) == "c")
print(baseConversion("6", 7) == "6")
print(baseConversion("337", 8) == "df")
