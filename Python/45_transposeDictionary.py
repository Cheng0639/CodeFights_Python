def transposeDictionary(scriptByExtension):
    return sorted([[scriptByExtension[i], i] for i in scriptByExtension])


print(transposeDictionary({
    "validate": "py",
    "getLimits": "md",
    "generateOutputs": "json"
}) == [["json", "generateOutputs"],
       ["md", "getLimits"],
       ["py", "validate"]])
