from itertools import takewhile, count


def floatRange(start, stop, step):
    # gen = map(lambda x: round(x,len(str(step).split('.')[1]) if len(str(step).split('.'))==2 else 0), takewhile(lambda x: x<stop ,count(start,step)))
    gen = takewhile( lambda x : x<stop,count(start,step))
    print(list(gen))
    return list(gen)


print(floatRange(-0.9, 0.45, 0.2))
print(floatRange(-0.9,0.45,0.2)==[-0.9, -0.7, -0.5, -0.3, -0.1, 0.1, 0.3])
print(floatRange(1.5,1.5,10)==[])
