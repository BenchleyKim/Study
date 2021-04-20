import sys 
sys.stdin = open("./Algorithm_Study/BOJ0304/BOJ1932", "r")

N = int(sys.stdin.readline())
Triangle = []
DP =  []
for i in range(1,N+1) :
  Triangle.append(list(map(int, sys.stdin.readline().split())))
  DP.append([0] * i)
DP[0][0] = Triangle[0][0]
for i in range(1,N) : # 1
  for j in range(i+1) : # 0 1
    if j == 0 :
      DP[i][j] = DP[i-1][j] + Triangle[i][j]
      continue
    if j == i :
      DP[i][j] = DP[i-1][j-1] + Triangle[i][j]
      continue
    DP[i][j] = max(DP[i-1][j], DP[i-1][j-1]) + Triangle[i][j]
print(max(DP[N-1]))