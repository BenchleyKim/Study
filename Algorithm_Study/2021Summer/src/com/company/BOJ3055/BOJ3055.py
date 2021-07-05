import sys
from collections import deque
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/company/BOJ3055/BOJ3055.in","r")
input = sys.stdin.readline

R, C = map(int, input().split())
board = []
for i in range(R) :
    board.append(list(input().rstrip()))


D = []
S = []
for r in range(R) :
    for c in range(C) :
        if board[r][c] == "D" :
            D = [r, c]
        if board[r][c] == "S" :
            board[r][c] = '.'
            S = [r, c]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0 
queue = deque()
queue.append(S)
check = [[0] * C for _ in range(R)]
while True :
    cnt += 1
    for i in range(R) :
        for j in range(C) :
            if board[i][j] == "*" :
                for d in range(4) :
                    nx, ny = i + dx[d] , j + dy[d]
                    if 0<= nx < R and 0 <= ny < C :
                        if board[nx][ny] == "." :
                            board[nx][ny] = ".*"
    for i in range(R) :
        for j in range(C) :
            if board[i][j] == '.*' :
                board[i][j] = "*"
        
    end_flag = False 
    if not queue :
        print("KAKTUS")
        break
    next_queue = deque()
    while queue :
        cx , cy = queue.popleft()
        if board[cx][cy] == "D" :
            end_flag = True
            break
        
        for d in range(4) :
            nx , ny = cx + dx[d], cy + dy[d] 
            if 0<= nx < R and 0 <= ny < C :
                if board[nx][ny] == "." or board[nx][ny] == 'D':
                    if check[nx][ny] :
                        continue
                    check[nx][ny] = 1
                    next_queue.append((nx,ny))
                    continue
    queue = next_queue
    if end_flag :
        print(cnt-1)
        break

