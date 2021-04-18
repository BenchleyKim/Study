import sys 
sys.stdin = open("./Algorithm_Study/STD0418/test03", "r")
input = sys.stdin.readline

# 첫 줄에 N, M, 그리고 초기 연료의 양이 주어진다. 
# (2 ≤ N ≤ 20, 1 ≤ M ≤ N2, 1 ≤ 초기 연료 ≤ 500,000) 
# 연료는 무한히 많이 담을 수 있기 때문에, 초기 연료의 양을 넘어서 충전될 수도 있다.

# 다음 줄부터 N개의 줄에 걸쳐 백준이 활동할 영역의 지도가 주어진다. 
# 0은 빈칸, 1은 벽을 나타낸다.

# 다음 줄에는 백준이 운전을 시작하는 칸의 행 번호와 열 번호가 주어진다. 
# 행과 열 번호는 1 이상 N 이하의 자연수이고, 운전을 시작하는 칸은 빈칸이다.

# 그다음 줄부터 M개의 줄에 걸쳐 각 승객의 출발지의 행과 열 번호, 그리고 목적지의 행과 열 번호가 주어진다. 
# 모든 출발지와 목적지는 빈칸이고, 모든 출발지는 서로 다르며, 각 손님의 출발지와 목적지는 다르다.

N , M , F = map(int, input().split())
board = [ ]
for i in range(N) :
    board.append(list(map(int, input().split())))

for b in board : 
    print(b)
sx, sy = map(int, input().split())
passegers = {}
for i in range(M) :
    px,py, dx,dy = list(map(int, input().split()))
    board[px-1][py-1], board[dx-1][dy-1] = 2,3 
    if passegers.get(px-1) :
        passegers[px-1][py-1] = [dx-1,dy-1]
    else :
        passegers[px-1] = {}
        passegers[px-1][py-1] = [dx-1,dy-1]

print(passegers)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

queue = [(sx-1,sy-1)]
check = [[0] * N for _ in range(N) ]
nxQueue = []
cnt = 0

for i in range(M):
    if F < 0 :
        break
    flag = True 
    dist = 0
    near = []
    check = [[0] * N for _ in range(N) ]    
    while flag :        
        dist += 1
        nextQueue = []
        for q in queue :
            cx, cy = q 
            if check[cx][cy] :
                continue
            check[cx][cy] = 1 
            for d in range(4) :
                nx, ny = cx+dx[d] , cy + dy[d]
                if 0<= nx < N and 0<= ny < N :
                    if board[nx][ny] == 1 :
                        continue
                    if board[nx][ny] == 3 :
                        continue
                    if board[nx][ny] == 2 :
                        flag = False
                        near.append((nx,ny))
                        continue
                    else :
                        nxQueue.append((nx,ny))
        if flag :
            queue = nxQueue
        else :
            near.sort()
    F -= dist
    px,py = near[0]
    dstx,dsty = passegers[px][py] 
    dist = 0 
    flag  = True
    check = [[0] * N for _ in range(N) ]   
    while flag :
        dist += 1
        nextQueue = []
        for q in queue :
            cx, cy = q 
            if check[cx][cy] :
                continue
            if cx == dstx and cy== dsty :
                cnt += 1
                flag = False
                break
            check[cx][cy] = 1 
            for d in range(4) :
                nx, ny = cx+dx[d] , cy + dy[d]
                if 0<= nx < N and 0<= ny < N :
                    if board[nx][ny] == 1 :
                        continue
                    if board[nx][ny] == 3 :
                        continue
                    if board[nx][ny] == 2 :
                        continue
                    nxQueue.append((nx,ny))
        if flag :
            queue = nxQueue
    F += dist 


if F < 0 :
    print(-1)
else :
    if cnt != M :
        print(-1)
    else :
        print(F)






            

