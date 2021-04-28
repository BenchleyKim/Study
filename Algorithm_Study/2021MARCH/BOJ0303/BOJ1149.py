import sys 
sys.stdin = open("./Algorithm_Study/BOJ0303/BOJ1149", "r")
N = int(sys.stdin.readline())
DP = [[0]*3 for i in range(N)]

for i in range(N) :
  R, G, B = map(int,sys.stdin.readline().split())
  if i == 0 :
    DP[i][0] = R
    DP[i][1] = G
    DP[i][2] = B
  else :
    DP[i][0] = min(DP[i-1][1],DP[i-1][2])+R
    DP[i][1] = min(DP[i-1][0],DP[i-1][2])+G
    DP[i][2] = min(DP[i-1][1],DP[i-1][0])+B

print(min(DP[-1]))