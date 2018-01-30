import re


def getCommit(commit):
    return commit.lstrip('0?+!')


def getCommit1(commit):
    print(re.sub("[0?+!]", '', commit))
    return re.sub("[0?+!]", '', commit)


print(getCommit("0??+0+!!someCommIdhsSt") == "someCommIdhsSt")
print(getCommit("noAUTHORofTHIScOmMiT") == "noAUTHORofTHIScOmMiT")
