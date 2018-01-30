import re

def longestDigitsPrefix(inputString):
    return re.findall("^\d*",inputString)[0]

print( longestDigitsPrefix("123aa1")=="123")
print( longestDigitsPrefix("0123456789")=="0123456789")
print( longestDigitsPrefix("12abc34")=="12")
print( longestDigitsPrefix("the output is 42")=="")
