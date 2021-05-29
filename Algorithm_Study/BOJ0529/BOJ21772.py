from os import rename
import sys
sys.stdin = open(".\Algorithm_Study\BOJ0529\BOJ21772","r")
input = sys.stdin.readline

R, C, T = map(int, input().split())
board = []
for i in range(R) :
    board.append(list(input().rstrip()))

cx = 0 
cy = 0
arr = []
for i in range(R) :
    for j in range(C) :
        if board[i][j] == 'G' :
            cx, cy = i, j
        if board[i][j] == 'S' :
            arr.append((i,j))
print(arr)
queue = [(cx,cy,0,[])] 
mx = 0
dx = [1,-1,0,0,0]
dy = [0,0,1,-1,0]
while queue :
    cx, cy , time, box = queue.pop(0)
    if time > T  :
        mx = max(mx, len(box))
        continue
    if board[cx][cy] == 'S' :
        if (cx,cy) in box :
            pass
        else :
            box = box + [(cx,cy)]
    for d in range(5) :
        nx, ny = cx+ dx[d], cy + dy[d]
        if 0<= nx < R and 0<= ny < C :
            if board[nx][ny] != '#' :
                queue.append((nx,ny,time+1, box))
print(mx)




