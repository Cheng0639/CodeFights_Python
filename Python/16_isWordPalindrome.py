def isWordPalindrome(word):
    return word == word[::-1]


print(isWordPalindrome("aibohphobia") == True)
print(isWordPalindrome("hehehehehe") == False)
print(isWordPalindrome("toot") == True)
print(isWordPalindrome("codedog") == False)
print(isWordPalindrome("z") == True)
print(isWordPalindrome("ilongpalindrome") == False)
print(isWordPalindrome("abacaba") == True)
