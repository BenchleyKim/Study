import sys
sys.stdin = open("./Algorithm_Study/BOJ0420/BOJ17626","r")
N=int(input())
l=int(N**(1/2))
DP=[i for i in range(N+1)]
for i in range(l+1) :
    DP[i**2] = 1
for i in range(1,l+1) :
    i = i**2
    for j in range(i,N+1-i) :
        DP[i+j] = min(DP[i+j], DP[i] + DP[j])
print(DP[N])