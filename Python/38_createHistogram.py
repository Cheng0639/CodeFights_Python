def createHistogram(ch, data):
    return map(lambda i: ch * i, data)


def createHistogram(ch, data):
    return [ch * i for i in data]


print(createHistogram('*', [12, 12, 14, 3, 12, 15, 14]) == ["************",
                                                            "************",
                                                            "**************",
                                                            "***",
                                                            "************",
                                                            "***************",
                                                            "**************"])
