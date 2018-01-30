def electionsWinners(votes, k):
    m = max(votes)
    return int(votes.count(m) == 1) if k == 0 else len([i for i in votes if i + k > m])


print(electionsWinners([2, 3, 5, 2], 3) == 2)
print(electionsWinners([1, 3, 3, 1, 1], 0) == 0)
print(electionsWinners([5, 1, 3, 4, 1], 0) == 1)
print(electionsWinners([1, 1, 1, 1], 1) == 4)
print(electionsWinners([1, 1, 1, 1], 0) == 0)
print(electionsWinners([3, 1, 1, 3, 1], 2) == 2)
