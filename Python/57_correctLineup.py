def correctLineup(athletes):
    return [ x for i in zip(athletes[1::2], athletes[::2]) for x in i ]


def correctLineup1(athletes):
    athletes[1::2], athletes[::2] = athletes[::2], athletes[1::2]
    return athletes


print(correctLineup([1, 2, 3, 4, 5, 6]) == [2, 1, 4, 3, 6, 5])
print(correctLineup([13, 42]) == [42, 13])
print(correctLineup([85, 32, 45, 67, 32, 12, 45, 67])
      == [32, 85, 67, 45, 12, 32, 67, 45])
