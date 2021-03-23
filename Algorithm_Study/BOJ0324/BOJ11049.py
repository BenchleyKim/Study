import sys
sys.stdin = open("./Algorithm_Study/BOJ0324/BOJ11049", "r")
input = sys.stdin.readline

N = int(input())
DP = [[0] * N for _ in range(N)]
arr = []
for _ in range(N) :
  arr.append(list(map(int, input().split())))
if N == 1 :
  print(arr[0][0] * arr[0][1])
  sys.exit()
for i in range(N-1) :
  DP[0][i] = arr[i][0] * arr[i][1] * arr[i+1][1]
for i in range(1,N-1) :
  for j in range(N-1-i) :
    if j + i > N :
      continue
    candidate1 = 1 
    candidate2 = 1
    for k in range(i+1):
      candidate1 *= arr[j+k+1][1]
      candidate2 *= arr[j+k][0]
    candidate1 *= arr[j][0] 
    candidate2 *= arr[j+i+1][1] 
    
    DP[i][j] = min(2**32-1, candidate1 + DP[i-1][j] , candidate2 + DP[i-1][j+1])
print(DP[N-2][0])
