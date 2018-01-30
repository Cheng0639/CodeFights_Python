from collections import Counter
def palindromeRearranging(inputString):
    return len([ v for v , i in Counter(inputString).items() if i %2==1])<2


print(palindromeRearranging("aabb")==True)
print(palindromeRearranging('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc')==False)