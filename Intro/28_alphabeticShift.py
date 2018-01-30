def alphabeticShift(inputString):
    return "".join(['a' if i == 'z' else chr(ord(i) + 1)for i in list(inputString)])


print(alphabeticShift("crazy") == "dsbaz")
print(alphabeticShift("z") == "a")
