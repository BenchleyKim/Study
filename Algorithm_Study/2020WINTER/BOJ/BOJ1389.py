import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ1389", "r")
INF = 100001
N , M = map(int, input().split())
R = [[INF]*(N+1) for _ in range(N+1)]
D = [[INF]*(N+1) for _ in range(N+1)]

for i in range(M) :
  A, B = map(int, input().split())
  R[A][B] = 1
  R[B][A] = 1 

for k in range(N+1) :
  for i in range(N+1) : 
    for j in range(N+1) :
      R[i][i] = 0
      if R[i][j] > R[i][k] + R[k][j]:
        R[i][j] = R[i][k] + R[k][j]
mn = INF
i = 0 
for idx, d in enumerate(R) :
  if mn > sum(d[1:]) :
    mn = sum(d[1:])
    i = idx
print(i)