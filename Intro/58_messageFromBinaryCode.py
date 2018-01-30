def messageFromBinaryCode(code):
    return "".join([chr(int(code[i * 8:i * 8 + 8], 2))for i in range(int(len(code) / 8))])


print(messageFromBinaryCode(
    "010010000110010101101100011011000110111100100001") == "Hello!")
print(messageFromBinaryCode("01001101011000010111100100100000011101000110100001100101001000000100011001101111011100100110001101100101001000000110001001100101001000000111011101101001011101000110100000100000011110010110111101110101") == "May the Force be with you")
print(messageFromBinaryCode("010110010110111101110101001000000110100001100001011001000010000001101101011001010010000001100001011101000010000001100000011010000110010101101100011011000110111100101110") == "You had me at `hello.")
