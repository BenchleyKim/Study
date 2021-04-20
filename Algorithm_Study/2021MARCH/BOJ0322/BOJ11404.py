import sys
sys.stdin = open("./Algorithm_Study/BOJ0322/BOJ11404", "r")
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = sys.maxsize
DP = [[INF] * N for _ in range(N)]
for _ in range(M) :
  A, B, C = map(int, input().split())
  DP[A-1][B-1] = min(DP[A-1][B-1], C)


for i in range(N) :
  DP[i][i] = 0
  for j in range(N) :
    for k in range(N) : 
      DP[j][k] = min(DP[j][k], DP[j][i] + DP[i][k])
for line in DP : 
  for element in line :
    if element == INF :
      element = 0
    print(element,end=' ')
  print(end='\n')

