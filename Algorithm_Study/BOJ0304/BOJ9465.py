import sys 
sys.stdin = open("./Algorithm_Study/BOJ0304/BOJ9465", "r")

T = int(sys.stdin.readline())
for _ in range(T) :
  N = int(sys.stdin.readline())
  table = []
  DP = [[0] * N for _ in range(2)]
  for _ in range(2) :
    table.append(list(map(int, sys.stdin.readline().split())))
  DP[0][0] = table[0][0]
  DP[1][0] = table[1][0]
  if N < 2 :
    print(max(DP[0][0], DP[1][0]))
    break
  DP[0][1] = table[0][1] + DP[1][0] 
  DP[1][1] = table[1][1] + DP[0][0] 
  
  for i in range(2,N) :
    DP[0][i] = max(DP[1][i-2],DP[1][i-1]) + table[0][i]
    DP[1][i] = max(DP[0][i-2],DP[0][i-1]) + table[1][i]
  print(max(DP[0][N-1],DP[1][N-1]))

