def twinsScore(b, m):
    return list(map(sum,zip(b,m)))

print(twinsScore([22, 13, 45, 32],[28, 41, 13, 32])==[50, 54, 58, 64])