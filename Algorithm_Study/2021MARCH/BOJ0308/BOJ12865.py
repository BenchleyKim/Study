import sys 
sys.stdin = open("./Algorithm_Study/BOJ0308/BOJ12865", "r")

N, K = map(int, sys.stdin.readline().split())
DP = [[0] * (K+1) for _ in range(N+1)]
item = [[0,0]]

start = N
start_idx = 0
for i in range(1,N+1) :
  W, V = map(int, sys.stdin.readline().split())
  if W < start :
    start = W
    start_idx = i
  if W >= K :
    item.append([0,0])
    continue
  DP[i][W] = V
  item.append([W,V])

for i in range(1,N+1) :
  for j in range(K, 0, -1) :
    if j >= item[i][0] :
      DP[i][j] = max(DP[i-1][j], item[i][1] + DP[i-1][j-item[i][0]])
    else :
      DP[i][j] = DP[i-1][j]
    
print(max(DP[N]))