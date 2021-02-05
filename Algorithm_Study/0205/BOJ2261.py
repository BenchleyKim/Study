import math
n = int(input())
pointList = []
for _ in range(n) :
  pointList.append(list(map(int,input().split())))

pointList.sort()
print(pointList)

def calDist(a, b):
  return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def devideAndConquer(s, e) :
  l = e -s
  if l == 2 :
    return calDist(pointList[s], pointList[e])
  if l == 3 :
    return min(calDist(pointList[s],pointList[e]), calDist(pointList[s],pointList[s+1]),calDist(pointList[s+1], pointList[e]))
  l //= 2
  left = devideAndConquer(s, l)
  right = devideAndConquer(l,e)
  return devideAndConquer