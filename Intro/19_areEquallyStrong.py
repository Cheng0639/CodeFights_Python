def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return (yourLeft == friendsLeft or yourLeft==friendsRight)and(yourRight == friendsRight or yourRight==friendsLeft)

print(areEquallyStrong(10,15,15,10)==True)
print(areEquallyStrong(15,10,15,10)==True)
print(areEquallyStrong(15,10,15,9)==False)
print(areEquallyStrong(20,15,5,20)==False)
