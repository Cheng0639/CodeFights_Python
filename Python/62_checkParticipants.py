def checkParticipants(participants):
    return [i for i, j in enumerate(participants) if j < i]


print(checkParticipants([0, 1, 1, 5, 4, 8]) == [2])
print(checkParticipants([0, 1, 2, 3, 4, 5]) == [])
print(checkParticipants([3, 3, 3, 3, 3, 3, 3, 3]) == [4, 5, 6, 7])
print(checkParticipants([0, 0, 1, 5, 5, 4, 5, 4, 10, 8]) == [1, 2, 5, 6, 7, 9])
