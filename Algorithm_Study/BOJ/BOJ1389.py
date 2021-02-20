import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ1389", "r")
INF = 100000
N , M = map(int, input().split())
R = [[0]*(N+1) for _ in range(N+1)]
D = [[INF]*(N+1) for _ in range(N+1)]

print(R)
for _ in range(M) :
  A, B = map(int, input().split())
  R[A][B] = 1
  R[B][A] = 1 
for r in R :
  print(r)
# for i in range(N+1) :
#   for j in range(N+1) :
for i in range(N) : 
  for j in range(N) :
    if i == j :
      D[i][j] = 0
      continue
    
    