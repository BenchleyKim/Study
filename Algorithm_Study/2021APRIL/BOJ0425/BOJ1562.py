import sys 
sys.stdin = open(".\Algorithm_Study\BOJ0425\BOJ1592","r")
input = sys.stdin.readline

N = int(input())
print(N)
DP = [0] * (N+1)
if N >= 10 : 
    DP[10] = 1
for i in range(11,N+1) :
    DP[i] = (DP[i-1] * 18) % 1000000000
print(sum(DP))


## N 이 10일 떄 
# 9, 8 , 7, 6, 5 , 4, 3, 2, 1, 0

## N이 11일 떄 + 2 
# 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1 

## N이 12일 때 + 4 
# (7,9), 8 ,9 , 8, 7, 6, 5, 4 , 3, 2, 1, 0,1, (0,2)