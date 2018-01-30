from collections import Counter


def frequencyAnalysis(encryptedText):
    return Counter(encryptedText).most_common(1)[0][0]


def frequencyAnalysis2(encryptedText):
    return sorted(Counter(encryptedText), key=Counter(encryptedText).get, reverse=True)[0]


def frequencyAnalysis1(encryptedText):
    return sorted({i: encryptedText.count(i) for i in set(encryptedText)}.items(), key=lambda x: x[1], reverse=True)[0][0]


print(frequencyAnalysis("$~NmiNmim$/NVeirp@dlzrCCCCfFfQQQ") == 'C')
print(frequencyAnalysis("Agoodglassinthebishop'shostelinthedevil'sseattwenty-onedegreesandthirteenminutesnortheastandbynorthmainbranchseventhlimbeastsideshootfromthelefteyeofthedeath's-headabeelinefromthetreethroughtheshotfiftyfeetout.") == 'e')
