import math
import sys
sys.setrecursionlimit(10**9)

n = int(input())
pointList = []
for _ in range(n) :
    pointList.append(list(map(int,input().split())))
pointList.sort()
# print(pointList)
# n = 10
# pointList = [[-7, -8], [-7, -7], [-2, -8], [0, 0], [1, 2], [2, 4], [3, 5], [7, 9], [50, 60], [70, 20]]

def calDist(a, b):
    return int((a[0] - b[0])**2 + (a[1] - b[1])**2)

def devideAndConquer(s, e) :
    # print(s, e)
    l = e -s
    if l == 1 :
        return calDist(pointList[s], pointList[e])
    if l == 2 :
        return min(calDist(pointList[s],pointList[e]), calDist(pointList[s],pointList[s+1]),calDist(pointList[s+1], pointList[e]))
    mid = (s + e) // 2
    left = devideAndConquer(s, mid)
    right = devideAndConquer(mid+1,e)
    d = min(left, right)
    midx = pointList[mid][0]
    check = []
    for i in pointList :
        if (i[0] - midx) ** 2 <= d :
            check.append(i)
    if len(check) <= 1 :
        return d
    check.sort(key = lambda x:x[1])
    # print(check)
    for i in range(len(check)-1) :
        for j in range(i+1, len(check)-1) :
            if (check[i][1] - check[j][1])**2 > d :
                break
            if check[i][0] < midx and check[j][0] < midx : 
                continue
            if check[i][0] > midx and check[j][0] > midx :
                continue
            d = min(d, calDist(check[i], check[j]))
    return d            
s = 0
e = len(pointList) -1 
# print(pointList)

print(devideAndConquer(s, e))

