def fixMessage(message):
    return message.capitalize()


print(fixMessage("you'll NEVER believe what that 'FrIeNd' of mine did!!1")
      == "You'll never believe what that 'friend' of mine did!!1")
print(fixMessage("i") == "I")
print(fixMessage("We are so doomed.") ==
      "We are so doomed.")
print(fixMessage("LOL you've GOT to hear this one XDD")
      == "Lol you've got to hear this one xdd")
