def validTime(time):
    h, s = map(int, time.split(':'))
    return h < 24 and s < 60


print(validTime("13:58") == True)
print(validTime("25:51") == False)
print(validTime("02:76") == False)
print(validTime("24:00") == False)
