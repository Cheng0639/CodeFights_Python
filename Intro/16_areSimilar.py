from collections import Counter

def areSimilar(a, b):
    return Counter(a)==Counter(b) and sum([a[i] != b[i]for i in range(len(a))]) <= 2


print(areSimilar([1, 2, 3], [1, 2, 3]) == True)
print(areSimilar([1, 2, 3], [2, 1, 3]) == True)
print(areSimilar([1, 2, 2], [2, 1, 1]) == False)
print(areSimilar([1, 1, 4],[1,2,3])==False)