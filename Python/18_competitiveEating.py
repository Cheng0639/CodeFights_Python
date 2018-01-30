def competitiveEating(t, width, precision):
    return ("{0:^{w}.{f}f}").format(t, w=width, f=precision)


print(competitiveEating(3.1415, 10, 2) == "   3.14   ")
print(competitiveEating(29.8245, 10, 0) == "    30    ")
print(competitiveEating(9.34, 4, 2) == "9.34")
print(competitiveEating(837.28472, 20, 7) == "    837.2847200     ")
print(competitiveEating(0, 4, 1) == "0.0 ")
print(competitiveEating(1, 3, 0) == " 1 ")
print(competitiveEating(666.2837, 15, 1) == "     666.3     ")
