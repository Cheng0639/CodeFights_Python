def isIPv4Address(inputString):
    l = inputString.split('.')
    return len(l) == 4 and len([i for i in l if i.isdigit() and (0 <= int(i) <= 255)]) == 4


print(isIPv4Address("172.16.254.1") == True)
print(isIPv4Address("172.316.254.1") == False)
print(isIPv4Address("0.1.0.0") == True)
print(isIPv4Address("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False)
