import sys 
sys.stdin = open("./Algorithm_Study/BOJ0427/BOJ1937","r")
input = sys.stdin.readline

N = int(input())
board = []
for i in range(N) :
    board.append(list(map(int, input().split())))
stack = [(0,0,0)]
DP = [[0]* N for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(N) :
    for j in range(N) :
        if DP[i][j] != 0 :
            continue
        stack = [(i,j,0)]
        print(stack)
        while stack :
            cx, cy, day = stack.pop()
            if DP[cx][cy] >= day :
                continue
            DP[cx][cy] = day
            for d in range(4) :
                nx, ny = cx+dx[d] , cy+dy[d]
                if 0<= nx < N and 0<=ny < N :
                    if board[nx][ny] < board[cx][cy] :
                        stack.append((nx,ny,day+1))

for b in DP :
    print(b)