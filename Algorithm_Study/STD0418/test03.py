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

sx, sy = map(int, input().split())

passegers = [0] * (M+2)

for i in range(2,M+2) :
    px,py, dx,dy = list(map(int, input().split()))
    board[px-1][py-1], board[dx-1][dy-1] = i,-i 
    passegers[i] = px-1,py-1,dx-1,dy-1
    

# print(passegers)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
queue = [(sx-1,sy-1)]
for b in board :
    print(b)

checkFlag = True

for i in range(M) :
    check = [[0]* N for _ in range(N)]
    near = []
    flag = True
    dist = 0
    print(queue,F)
    while flag :
        nq = []
        if len(queue) == 0 : 
            checkFlag = False
            break
        for q in queue :
            cx,cy = q 
            if check[cx][cy] :
                continue
            check[cx][cy] = 1
            if board[cx][cy] > 0 :
                near.append((cx,cy))
                flag = False
                continue
            for d in range(4) :
                nx, ny = cx+dx[d], cy+dy[d] 
                if 0<= nx < N and 0<= ny<N  :
                    if board[nx][ny] != 1 :
                        nq.append((nx,ny))
        if flag :
            dist += 1
            queue = nq[:]
    if F < dist :
        F -= dist
        break
    F -= dist
    near.sort()
    sx,sy = near[0]
    dst = board[sx][sy]
    board[sx][sy] = 0
    queue = [(sx,sy)]

    check = [[0]* N for _ in range(N)]
    tmp = 0
    flag = True
    dist = 0
    checkFlag = True
    # print(queue)
    while flag :
        nq = []
        if len(queue) == 0 :
            checkFlag = False
            break

        
        for q in queue :
            cx,cy = q 
            if check[cx][cy] :
                continue
            check[cx][cy] = 1
            if board[cx][cy] == -dst:
                tmp = (cx,cy)
                flag = False
                break
            for d in range(4) :
                nx, ny = cx+dx[d], cy+dy[d] 
                if 0<= nx < N and 0<= ny< N  :
                    if board[nx][ny] != 1 :
                        nq.append((nx,ny))
        if flag :
            dist += 1
            queue = nq[:]
    if F < dist :
        F -= dist
        break
    F += dist
    cx, cy=  tmp
    queue = [tmp]
    board[cx][cy] = 0
    if checkFlag == False :
        break

if F < 0 :
    print(-1)
else :
    if checkFlag :
        print(F)
    else :
        print(-1)





        








            

