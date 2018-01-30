def circleOfNumbers(n, firstNumber):
    return (firstNumber + n / 2) % n


print(circleOfNumbers(10, 2) == 7)
print(circleOfNumbers(10, 7) == 2)
print(circleOfNumbers(4, 1) == 3)
print(circleOfNumbers(6, 3) == 0)
