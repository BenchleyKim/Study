import sys
sys.stdin = open(".\Algorithm_Study\BOJ0510\BOJ21736","r")
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

x = y = 0
for i in range(N) :
    for j in range(M) :
        if board[i][j] == 'I' :
            x, y = i,j
dx = [1,-1,0,0]
dy = [0,0,1,-1]
check = [[0] * M for _ in range(N)]
stack  = [(x,y)]
ans = 0
while stack :
    cx, cy = stack.pop()
    if check[cx][cy] :
        continue
    check[cx][cy] = 1 
    if board[cx][cy] == 'P' :
        ans += 1
    for d in range(4 ) :
        nx , ny = cx+dx[d], cy+dy[d]
        if 0<= nx < N and 0<=ny < M :
            if board[nx][ny] in 'OP' :
                stack.append((nx,ny))
if ans :
    print( ans)
else:
    print('TT')