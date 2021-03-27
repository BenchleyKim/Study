import sys 
sys.stdin = open("./Algorithm_Study/0321/BOJ2747", "r")
input = sys.stdin.readline

N = int(input())
DP = [0] * (N+1)
DP[0] = 0
if N == 0 :
    print(0)
    exit()
if N == 1:
    print(1)
    exit()
if N == 2 :
    print(1)
    exit()
if N > 2 :
    DP[1] = DP[2] = 1
for i in range(3,N+1) :
    DP[i] = DP[i-1] + DP[i-2]
print(DP[N])

