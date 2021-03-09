import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ20543", "r")

def bombExplore(x, y):
    X_min, X_max = x - m , x + m 
    y_min, y_max = y - m , y + m
    if X_min <= 0 : X_min = 0
    if X_max > n : X_max = n -1 
    if y_min <= 0 : y_min = 0
    if y_max > n : y_max = n -1 
    for i in range(X_min, X_max+1):
        for j in range(y_min, y_max+1):
            h[i][j] += 1

n, m = list(map(int, sys.stdin.readline().rstrip().split()))
m = m//2

h = []
for i in range(n):
    h.append(list(map(int, sys.stdin.readline().rstrip().split())))

answer = [[0 for x in range(n)] for x in range(n)]

for x in range(m,n-m) :
    for y in range(m,n-m):
        k = -h[x-m][y-m]
        answer[x][y] = k
        for i in range(k):
            bombExplore(x,y)

for i in answer:
    for j in i :
      print(j, end = ' ')
    print()