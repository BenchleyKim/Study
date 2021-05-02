import sys 
from itertools import permutations
sys.stdin = open(".\Algorithm_Study\BOJ0428\BOJ2225","r")
input = sys.stdin.readline

N, K = map(int, input().split())
DP = [[0]* (K+1) for i in range(N+1)]
mod = 1000000000
for i in range(1,K+1) :
    DP[0][i] = 1 
for i in range(1, N+1) :
    for j in range(K+1) :
        DP[i][j] = (DP[i-1][j]+DP[i][j-1])%mod
print(DP[N][K]%mod)
