def twoTeams(students):
    return sum(students[::2]) - sum(students[1::2])


print(twoTeams([1, 11, 13, 6, 14]) == 11)
print(twoTeams([3, 4]) == -1)
print(twoTeams([16, 14, 79, 8, 71, 72, 71,
                10, 80, 76, 83, 70, 57, 29, 31]) == 209)
print(twoTeams([23, 72, 54, 4, 88, 91, 8, 44]) == -38)
print(twoTeams([23, 74, 57, 33, 61, 99, 19, 12, 19, 38, 77, 70, 20]) == -50)
