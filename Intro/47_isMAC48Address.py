import re


def isMAC48Address(inputString):
    return bool(re.match("^([0-9A-F]{2}-){5}[0-9A-F]{2}$", inputString))


print(isMAC48Address("00-1B-63-84-45-E6") == True)
print(isMAC48Address("Z1-1B-63-84-45-E6") == False)
print(isMAC48Address("not a MAC-48 address") == False)
print(isMAC48Address("FF-FF-FF-FF-FF-FF") == True)
print(isMAC48Address("00-00-00-00-00-00") == True)
print(isMAC48Address("G0-00-00-00-00-00") == False)
print(isMAC48Address("02-03-04-05-06-07-") == False)
print(isMAC48Address("12-34-56-78-9A-BC") == True)
