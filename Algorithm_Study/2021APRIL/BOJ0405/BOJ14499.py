import sys

sys.stdin = open("./Algorithm_Study/BOJ0405/BOJ14499", "r")
input = sys.stdin.readline

N,M,X,Y,K = map(int, input().split())
board = []
for i in range(N) :
    board.append(list(map(int, input().split())))
commands = list(map(int, input().split()))
dx = [0,0,-1,1]
dy = [1,-1,0,0]
dice_row = [0,0,0]
dice_col = [0,0,0,0]
def roll(dt) :
    # 오른쪽으로 굴렸을떄
    if dy[dt] > 0 :
        dice_row.insert(0,dice_col.pop())
        dice_col.append(dice_row.pop())
        dice_col[1] = dice_row[1]
        # ex ) [6,4,1] , [2,1,5,3]
    # 왼쪽으로 굴렸을 떄     
    if dy[dt] < 0 :
        dice_row.append(dice_col.pop())
        dice_col.append(dice_row.pop(0))
        dice_col[1] = dice_row[1]
        # ex) [1,3,6] , [2,1,5,4]
    # 위로 굴렸을 때 
    if dx[dt] < 0 :
        dice_col.append(dice_col.pop(0))
        dice_row[1] = dice_col[1]
    if dx[dt] > 0 :
        dice_col.insert(0,dice_col.pop())
        dice_row[1] = dice_col[1]
board[X][Y] = 0 
while commands :
    dt = commands.pop(0)
    dt -= 1
    if X+dx[dt] >= N or X+dx[dt] < 0 or Y+dy[dt] < 0 or Y+dy[dt]>= M :
        continue
    X,Y = X+dx[dt], Y+dy[dt]
    # print(X,Y)
    roll(dt) 
    if board[X][Y] != 0 :
        dice_col[3] = board[X][Y] 
        board[X][Y] = 0
    else :
        board[X][Y] = dice_col[3]
    print(dice_col[1])

