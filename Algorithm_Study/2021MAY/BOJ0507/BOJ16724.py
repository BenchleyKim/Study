import sys
sys.stdin = open(".\Algorithm_Study\BOJ0507\BOJ16724","r")
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for i in range(N) :
    board.append(list(input().rstrip()))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
direct = {'U' : 0, 'D': 1 , 'L' : 2 ,'R' : 3}
check = [[(i,j) for j in range(M)] for i in range(N)]
check = [[0]*M for _ in range(N)]
# for c in check :
#     print(c)
rootcheck = {}
cnt = 0
for i in range(N) :
    for j in range(M) :
        # 다음 위치 
        if check[i][j] :
            continue
        cnt += 1
        check[i][j] = cnt
        cd = direct[board[i][j]]
        nx ,ny = i+dx[cd], j + dy[cd]
        while check[nx][ny] == 0 :
            if nx == i and ny == j :
                break
            check[nx][ny] = cnt
            nd = direct[board[nx][ny]]
            nx , ny = nx + dx[nd], ny + dy[nd]
        if check[nx][ny] == cnt :
            rootcheck[cnt] = cnt
            continue
        else :
            rootcheck[cnt] = check[nx][ny]
answer = 0
for ke in rootcheck.keys() :
    if rootcheck[ke] == ke :
        answer += 1
for c in check :
    print(c)
print(answer)











        
