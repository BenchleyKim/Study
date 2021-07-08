import sys
sys.stdin = open("./Algorithm_Study/BOJ0708/BOJ11051.in","r")
input = sys.stdin.readline

MOD = 10_007
N , K = map(int, input().split())
print(N,K)
DP = [[1] * (K + 1) for _ in range(N+1)]
for i in range(1,N+1) :
    for j in range(1,K+1) :
        if i == j :
            DP[i][j] = 1
            continue
        DP[i][j] = (DP[i-1][j] + DP[i-1][j-1]) 

print(DP[N][K] % MOD)