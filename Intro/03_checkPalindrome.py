def checkPalindrome(inputString):
    return inputString == inputString[::-1]


print(checkPalindrome("aabaa") == True)
print(checkPalindrome("abac") == False)
print(checkPalindrome("a") == True)
print(checkPalindrome("az") == False)
print(checkPalindrome("abacaba") == True)
print(checkPalindrome("aaabaaaa") == False)
print(checkPalindrome("zzzazzazz") == False)
print(checkPalindrome("hlbeeykoqqqqokyeeblh") == True)
