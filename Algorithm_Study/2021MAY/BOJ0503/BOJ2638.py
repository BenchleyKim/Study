import sys 
sys.stdin = open(".\Algorithm_Study\BOJ0503\BOJ2638","r")
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for i in range(N) :
    board.append(list(map(int, input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0
stack = [(0,0)]
check = [[0]*M for _ in range(N)]
while stack :
    x, y = stack.pop()
    if check[x][y] :
        continue
    check[x][y] = 1
    board[x][y] = 2
    for d in range(4) :
        nx, ny = x+dx[d], y+dy[d]
        if 0<= nx < N and 0<= ny < M :
            if board[nx][ny] == 0 :
                stack.append((nx,ny))
while True :
    flag = True
    nboard = [[0]*M for _ in range(N)]
    for i in range(1,N-1) :
        for j in range(1,M-1) :
            if board[i][j] == 1 :
                flag = False
                ncnt = 0
                for d in range(4) :
                    nx, ny = i+dx[d], j+dy[d]
                    if board[nx][ny] == 2 :
                        ncnt += 1
                if ncnt < 2 :
                    nboard[i][j] = 1 
                else :
                    nboard[i][j] = 0
    if flag :
        print(cnt)
        break
    stack = [(0,0)]
    check = [[0]*M for _ in range(N)]
    while stack :
        x, y = stack.pop()
        if check[x][y] :
            continue
        check[x][y] = 1
        nboard[x][y] = 2
        for d in range(4) :
            nx, ny = x+dx[d], y+dy[d]
            if 0<= nx < N and 0<= ny < M :
                if nboard[nx][ny] == 0 :
                    stack.append((nx,ny))
    cnt += 1
    board = nboard

                
