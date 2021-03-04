import sys 
sys.stdin = open("./Algorithm_Study/BOJ0304/BOJ12865", "r")
N, K = map(int, sys.stdin.readline().split())
memo = [[0] * (K+1) for _ in range(N+1)]
items = []
for i in range(N) :
  W, V = map(int, sys.stdin.readline().split())
  items.append((W,V))
  memo[i+1][W] = V 
  

for n in range(1,N+1) :
  for k in range( items[n-1][0], K+1) :
    memo[n][k] = max(memo[n-1][k],memo[n][k-1]) + items[n-1][1]
for m in memo :
  print(m)