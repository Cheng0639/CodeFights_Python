def convertTabs(code, x):
    return code.replace('\t', ' ' * x)


print(convertTabs("\treturn False", 4) == "    return False")
print(convertTabs("", 8) == "")
print(convertTabs("    for x in range(20)", 16) == "    for x in range(20)")
print(convertTabs("def add(x, y)\n\treturn x + y", 8) == "def add(x, y)\n        return x + y"
      )
print(convertTabs("\t\t\t\t\t", 4) == "                    ")
