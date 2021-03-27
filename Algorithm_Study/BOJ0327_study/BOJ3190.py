import sys 
sys.stdin = open("./Algorithm_Study/BOJ0327_study/BOJ3190", "r")
input = sys.stdin.readline

N = int(input())
board = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K) :
    X, Y = map(int, input().split())
    board[X-1][Y-1] = 1
L = int(input())
commands = []
for _ in range(L) :
    X, C = input().split()
    X = int(X)
    commands.append((X,C))
dx = [0,1,0,-1]
dy = [1,0,-1,0]
# 머리 위치 , 꼬리 위치, 방향
time = 0
snake = [(0,0)]
board[0][0] = 9 
d = 0
while True :
    time += 1
    # print(time, snake)
    if not commands :
        pass
    else :
        if (time-1)== commands[0][0]:
            X, C = commands.pop(0)
            if C == 'D' :
                d = (d+1)%4
            elif C == 'L' :
                d = (d+3)%4
    hx,hy,= snake[0]
    nx , ny = hx + dx[d] , hy+dy[d]
    if nx < 0 or nx >= N or ny < 0 or ny >= N :
        break
    if board[nx][ny] == 9 :
        break
    snake.insert(0,(nx,ny))
    if board[nx][ny] == 1 : 
        pass
    else :
        tx,ty = snake.pop()
        board[tx][ty] = 0
    board[nx][ny] = 9

print(time)    

        

    
    