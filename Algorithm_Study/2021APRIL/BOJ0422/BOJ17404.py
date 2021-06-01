import sys
sys.stdin = open("./Algorithm_Study/BOJ0422/BOJ17404","r")
input = sys.stdin.readline

N = int(input())
board = []
for i in range(N) :
    board.append(list(map(int, input().split())))
DP = [[0,0,0] for i in range(N)]

INF = sys.maxsize
ans = INF
for first in range(3) :
    for i in range(3) :
        if first == i :
            DP[0][i] = board[0][i]
        else : 
            DP[0][i] = INF
    for i in range(1,N) :
        DP[i][0] = board[i][0] + min(DP[i-1][1], DP[i-1][2])
        DP[i][1] = board[i][1] + min(DP[i-1][0], DP[i-1][2])
        DP[i][2] = board[i][2] + min(DP[i-1][1], DP[i-1][0])
    for i in range(3) :
        if i == first :
            continue
        else :
            ans = min(ans, DP[N-1][i])
print(ans)
