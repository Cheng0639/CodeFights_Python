def variableName(name):
    return name.isidentifier()


print(variableName("var_1__Int") == True)
print(variableName("qq-q") == False)
print(variableName(" variable") == False)
print(variableName("va[riable0") == False)
print(variableName("variable0") == True)
