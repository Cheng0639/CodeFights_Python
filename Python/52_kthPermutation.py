from itertools import permutations,islice


def kthPermutation(numbers, k):
    return list(next(islice(permutations(numbers),k-1,k)))

print(kthPermutation([1, 2, 3, 4, 5], 4) == [1, 2, 4, 5, 3])
print(kthPermutation([11, 22, 31, 43, 56], 120) == [56, 43, 31, 22, 11])
print(kthPermutation([14, 25, 27, 29, 30, 40, 55, 89, 100, 239], 238) == [
      14, 25, 27, 29, 40, 239, 100, 55, 89, 30])
