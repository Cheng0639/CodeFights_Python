import string


def isBeautifulString(inputString):
    tmp = [inputString.count(i) for i in string.ascii_lowercase]
    return tmp == sorted(tmp, reverse=True)


print(isBeautifulString("bbbaacdafe") == True)
print(isBeautifulString("aabbb") == False)
print(isBeautifulString("bbc") == False)
print(isBeautifulString("bbbaa") == False)
print(isBeautifulString("abcdefghijklmnopqrstuvwxyzz") == False)
print(isBeautifulString("abcdefghijklmnopqrstuvwxyz") == True)
print(isBeautifulString("zaa") == False)
