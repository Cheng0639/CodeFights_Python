def centuryFromYear(year):
    return (int)(year / 100) + (0 if year % 100 == 0 else 1)


print(centuryFromYear(1905))
