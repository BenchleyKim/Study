import sys 
from collections import deque
sys.stdin = open("./Algorithm_Study/BOJ0430/BOJ2573","r")
input = sys.stdin.readline

N , M  = map(int, input().split())
board = []
for i in range(N) :
    board.append(list(map(int, input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = 0 
while True :
    check = [[-1]*M for _ in range(N)]
    cnt = 0
    flag = True

    for i in range(N) :
        if not flag :
            break
        for j in range(M) :
            if board[i][j] == 0 :
                continue
            if check[i][j] != -1 :
                continue
            cnt += 1 
            # print(i,j,cnt)
            if cnt > 1 :
                flag = False
                break
            

            stack = deque([(i,j)])
            while stack :
                cx,cy = stack.popleft()
                if check[cx][cy] != -1 :
                    continue
                melt = 0
                for d in range(4) :
                    nx,ny= cx+dx[d] , cy+dy[d]
                    if 0<= nx < N and 0 <= ny < M :
                        if check[nx][ny] != -1 :
                            continue
                        if board[nx][ny] == 0 :
                            melt += 1
                        else :
                            stack.append((nx,ny))
                board[cx][cy] = max(0,board[cx][cy]-melt)
                check[cx][cy] = 1
    if not flag :
        print(ans)
        break
    ans += 1
    # for i in range(N) :
    #     for j in range(M) :
    #         if board[i][j] == 0 :
    #             continue
    #         board[i][j] -= check[i][j]
    #         board[i][j] = max(board[i][j], 0)


    