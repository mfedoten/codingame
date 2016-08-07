import math

LON = raw_input()
LAT = raw_input()
N = int(raw_input())

DEFIB = [raw_input().split(';') for i in xrange(N)]

lonUser = float(LON.replace(',','.')) * math.pi / 180
latUser = float(LAT.replace(',','.')) * math.pi / 180

distance = []
for i in xrange(N):
    lonDefib = float(DEFIB[i][-2].replace(',','.')) * math.pi / 180
    latDefib = float(DEFIB[i][-1].replace(',','.')) * math.pi / 180
    x = (lonUser - lonDefib) * math.cos((latUser + latDefib)/2)
    y = (latUser - latDefib)
    distance.append(math.sqrt(x**2 + y**2) * 6371)

closest = distance.index(min(distance))
answer = DEFIB[closest][1]

print answer
