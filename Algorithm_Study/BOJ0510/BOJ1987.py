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


import sys 
sys.setrecursionlimit(10000) 
def dfs(x, y, cnt): 
    dx = [1, -1, 0, 0] 
    dy = [0, 0, 1, -1] 
    now = (x, y) 
    global ans 
    ans = max(ans, cnt) 
    for i in range(4): 
        nx = now[0] + dx[i] 
        ny = now[1] + dy[i] 
        if(0 <= nx < R) and (0 <= ny < C): 
            if(done[strings[nx][ny]] == 0): 
                done[strings[nx][ny]] = 1 
                # print(done) 
                dfs(nx, ny, cnt+1) 
                done[strings[nx][ny]] = 0 #백트래킹 
R, C = map(int, input().split()) 
strings = [list(map(lambda x: ord(x)-65, input())) for _ in range(R)] # 아스키 코드로 바꿔줌 
done = [0]*26 # 알파벳 26개만큼 배열설정 
done[strings[0][0]] = 1 
ans = 1 
dfs(0, 0, ans) 
print(ans)

