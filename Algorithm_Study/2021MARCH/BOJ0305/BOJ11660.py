import sys 
sys.stdin = open("./Algorithm_Study/BOJ0305/BOJ11660", "r")

N ,M = map(int, sys.stdin.readline().split())
table =[]
for _ in range(N) :
  table.append(list(map(int, sys.stdin.readline().split())))


DP = [[0] * N for _ in range(N)]
DP[0][0] = table[0][0]
for i in range(1,N) :
  DP[0][i] = DP[0][i-1] + table[0][i]
for i in range(1,N) :
  for j in range(N) :
    if j == 0 :
      DP[i][j] = DP[i-1][j] + table[i][j]
      continue
    DP[i][j] =  DP[i-1][j] + DP[i][j-1] + table[i][j] -DP[i-1][j-1] 
for _ in range(M) :
  x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
  if x1-2 < 0 and y1-2 < 0 :
    result = DP[x2-1][y2-1]
  elif x1-2 < 0 :
    result = DP[x2-1][y2-1] - DP[x2-1][y1-2]
  elif y1-2 < 0 :
    result = DP[x2-1][y2-1] - DP[x1-2][y2-1]
  else :
    result = DP[x2-1][y2-1] - DP[x1-2][y2-1] - DP[x2-1][y1-2] + DP[x1-2][y1-2]
  print(result) 