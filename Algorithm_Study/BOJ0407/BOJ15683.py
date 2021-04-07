import sys
import copy
sys.stdin = open("./Algorithm_Study/BOJ0407/BOJ15683", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for i in range(N) :
    board.append(list(map(int, input().split())))

cctvs = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = 0
cctv5s = []
total = 0
for i in range(N) :
    for j in range(M) :
        if board[i][j] == 6 or board[i][j] == 0:
            if board[i][j] == 0 :
                total += 1

            continue
        if board[i][j] == 5  :
            cctv5s.append((i,j))
            continue
        else :
            cctvs.append((i,j,board[i][j]))


direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[3, 0], [0, 2], [2, 1], [1, 3]], 
[[1, 3, 0], [3, 0, 2], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]

def check(x,y,board,darr) :
    new_count  = 0
    for d in darr :
        nx, ny = x, y
        while True :
            nx, ny = nx+dx[d], ny+dy[d]
            if 0<= nx <N and 0<= ny <M :
                if board[nx][ny] == 6 :
                    break
                elif board[nx][ny] == 0 :
                    new_count += 1
                    board[nx][ny] = '#'
            else: 
                break
    return new_count

def dfs(board,cnt,result) :
    global ans
    if cnt == len(cctvs) :
        ans = max(result , ans)
        return
    x,y,cctv_cat = cctvs[cnt]
    for i in direction[cctv_cat] :
        new_board = copy.deepcopy(board) 
        res = check(x,y,new_board,i)
        dfs(new_board,cnt+1,result+res)

ans = 0
start_count = 0
for cctv5 in cctv5s :
    x,y = cctv5
    start_count += check(x,y,board,direction[5][0])
    
dfs(board,0,start_count)

print(total-ans)


