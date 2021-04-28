import sys
sys.stdin = open("./Algorithm_Study/BOJ0320/BOJ10942", "r")
input = sys.stdin.readline
N = int(sys.stdin.readline())
N = int(input())
arr = list(map(int,input().split()))
DP = [[0] * N for _ in range(N)]
for i in range(N) :
  DP[i][i] = 1 
for i in range(N-1) :
  if arr[i] == arr[i+1] :
    DP[i][i+1] = 1
for l in range(2,N) :
  for i in range(N-l) :
    if arr[i] == arr[i+l] and DP[i+1][i+l-1] == 1 :
      DP[i][i+l] = 1

M = int(input())
for _ in range(M) :
  S, E = map(int, input().split())
  print(DP[S-1][E-1])