
import sys
sys.stdin = open(".\Algorithm_Study\BOJ0523\sol01","r")
input = sys.stdin.readline

R, C = map(int, input().split())
Rg, Cg, Rp, Cp = map(int,input().split())
board = []
for i in range(R) :
    board.append(list(input().rstrip()))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0 
check = [[0] * C for _ in range(R)]
for i in range(R) :
    for j in range(C) :
        if board[i][j] == 'P' :
            if check[i][j] :
                continue
            stack = [(i,j)]
            while stack :
                
                cx, cy = stack.pop()
                if check[cx][cy] :
                    continue
                cnt += 1
                check[cx][cy] = 1 
                for d in range(4) :
                    nx , ny = cx+dx[d], cy+dy[d]
                    if 0<= nx < R and 0<= ny < C :
                        if board[nx][ny] == 'P' :
                            stack.append((nx,ny))

if cnt == Rp * Cp :
    print(0)
else :
    print(1)