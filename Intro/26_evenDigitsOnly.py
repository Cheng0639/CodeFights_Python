def evenDigitsOnly(n):
    return all([int(i) % 2 == 0 for i in str(n)])


print(evenDigitsOnly(248622) == True)
print(evenDigitsOnly(642386) == False)
print(evenDigitsOnly(1) == False)
print(evenDigitsOnly(8) == True)
print(evenDigitsOnly(2462487) == False)
print(evenDigitsOnly(468402800) == True)
print(evenDigitsOnly(5468428) == False)
