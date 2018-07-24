def brothersInTheBar(glasses):
    round_counter = 0
    index = 0
    while index < len(glasses)-2 and len(glasses) > 2:
        if len(set(glasses[index:index+3])) == 1:
            del glasses[index:index+3]
            round_counter += 1
            index = max(0, index-2)
        else:
            index += 1

    return round_counter