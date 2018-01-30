def buildPalindrome(st):
    reverse = st[::-1]
    count = len(reverse)

    while(st.rfind(reverse[0:count]) == -1):
        count -= 1

    return st[:st.rindex(reverse[0:count])] + reverse


print(buildPalindrome("abcdc") == "abcdcba")
print(buildPalindrome("ababab") == "abababa")
print(buildPalindrome("abba") == "abba")
print(buildPalindrome("abaa") == "abaaba")
