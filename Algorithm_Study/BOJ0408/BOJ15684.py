import sys
import copy
sys.stdin = open("./Algorithm_Study/BOJ0408/BOJ15684", "r")
input = sys.stdin.readline

N , M , H = map(int, input().split())
board = [[-1]*N for _ in range(H)]

for i in range(M) :
    a, b = map(int, input().split())
    board[a-1][b-1], board[a-1][b] = b,b-1

def check(board) :
    # N = 5 
    flag = True
    for i in range(N) :
        x ,y = 0, i
        while x < H :
            if board[x][y] != -1 :
                y = board[x][y]
                x += 1
            else :
                x += 1
            
        if y == i :
            continue
        else :
            flag = False
            break
    # 모두 일치하면 True 아니면 False 
    return flag

candidates = []
for i in range(H) :
    for j in range(N) :
        if board[i][j] != -1 :
            continue
        if j+1 < N :
            if board[i][j+1] == -1 :
                candidates.append((i,j,i,j+1))
if check(board) :
    print(0)
    sys.exit()
endflag = True
for candidate in candidates :
    i,j,ni,nj = candidate 
    board[i][j] , board[ni][nj] = nj, j
    if check(board) :
        print(1)
        sys.exit()
    board[i][j] = board[ni][nj] = -1

for idx in range(len(candidates)) :
    i,j,ni,nj = candidates[idx] 
    board[i][j] , board[ni][nj] = nj , j
    for jdx in range(idx+1,len(candidates)) :
        i2,j2,ni2,nj2 = candidates[jdx] 
        if board[i2][j2] != -1 or board[ni2][nj2] != -1 :
            continue
        board[i2][j2] , board[ni2][nj2] = nj2, j2
        # print()
        # for b in board :
        #     print(b)
        if check(board) :
            print(2)
            sys.exit()
        board[i2][j2] = board[ni2][nj2] = -1
    board[i][j] = board[ni][nj] = -1

for idx in range(len(candidates)) :
    i,j,ni,nj = candidates[idx] 
    board[i][j] , board[ni][nj] = nj , j
    for jdx in range(idx+1,len(candidates)) :
        i2,j2,ni2,nj2 = candidates[jdx] 
        if board[i2][j2] != -1 or board[ni2][nj2] != -1 :
            continue
        board[i2][j2] , board[ni2][nj2] = nj2, j2
        for kdx in range(jdx+1, len(candidates)) :
            i3,j3,ni3,nj3 = candidates[kdx] 
            if board[i3][j3] != -1 or board[ni3][nj3] != -1 :
                continue
            board[i3][j3] , board[ni3][nj3] = nj3, j3
            # print()
            # for b in board :
            #     print(b)
            if check(board) :
                print(3)
                sys.exit()
            board[i3][j3] = board[ni3][nj3] = -1

        board[i2][j2] = board[ni2][nj2] = -1
    board[i][j] = board[ni][nj] = -1

print(-1)

            



