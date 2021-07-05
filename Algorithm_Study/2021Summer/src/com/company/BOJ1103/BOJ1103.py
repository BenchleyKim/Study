import sys
from collections import deque
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/company/BOJ1103/BOJ1103.in","r")
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(str(input().rstrip())) for _ in range(N)]
check = [[0] * M for _ in range(N)]
DP = [[0] * M for _ in range(N)]

dx , dy = [1,-1, 0 ,0] , [0,0, 1, -1]
check[0][0] = 1 
answer = 0
def dfs(x,y, cnt) :
    global answer
    answer = max(answer, cnt)
    j = int(board[x][y])
    for d in range(4) :
        nx, ny  = x + (dx[d] * j) , y + (dy[d] * j)
        if 0<= nx < N and 0<= ny < M :
            if board[nx][ny] == 'H' :
                continue
            if DP[nx][ny] >= cnt + 1 :
                continue
            if check[nx][ny] :
                print(-1)
                exit()
            DP[nx][ny] = cnt + 1
            check[nx][ny] = 1 
            dfs(nx,ny, cnt + 1)
            check[nx][ny] = 0
dfs(0,0,1)

print(answer)
