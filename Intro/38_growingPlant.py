import math

def growingPlant(upSpeed, downSpeed, desiredHeight):
    return 1 if upSpeed > desiredHeight else math.floor(desiredHeight / (upSpeed - downSpeed))

print(growingPlant(100,10,910)==10)
print(growingPlant(10,9,4)==1)