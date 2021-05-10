import sys
import string
sys.stdin = open(".\Algorithm_Study\BOJ0510\BOJ1987","r")
input = sys.stdin.readline

R, C = map(int , input().split())
board = []
for r in range(R) :
    board.append(list(input().rstrip()))
alpha =list(string.ascii_uppercase)
alpha = {i : 0 for i in alpha}
stack = [(0,0,0)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
mx = 0
def dfs(cx,cy, cnt) :
    global mx
    if cnt == 26 :
        mx = 26 
        return
    mx = max(mx,cnt)
    for d in range(4) :
        nx , ny = cx+dx[d], cy+dy[d]
        if 0<= nx < R and 0<= ny < C :
            na = board[nx][ny] 
            if alpha[na] :
                continue
            else :
                alpha[na] = 1
                dfs(nx,ny,cnt + 1)
                alpha[na] = 0
alpha[board[0][0]] = 1
dfs(0,0,1)
print(mx)