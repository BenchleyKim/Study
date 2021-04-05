import sys

sys.stdin = open("./Algorithm_Study/BOJ0405/BOJ14499", "r")
input = sys.stdin.readline

N,M,X,Y,K = map(int, input().split())
board = []
for i in range(N) :
    board.append(list(map(int, input().split())))

for b in board :
    print(b)
dice = []
commands = list(map(int, input().split()))
print(commands)
dx = [0,0,-1,1]
dy = [1,-1,0,0]
dice_row = [4,1,3]
dice_col = [2,1,5,6]
# dice_row = [0,0,0]
# dice_col = [0,0,0,0]
def roll(dt) :
    dt -= 1
    # 오른쪽으로 굴렸을떄
    if dy[dt] > 0 :
        dice_row.insert(0,dice_col.pop())
        dice_col.append(dice_row.pop())
        # ex ) [6,4,1] , [2,1,5,3]
    # 왼쪽으로 굴렸을 떄     
    if dy[dt] < 0 :
        dice_row.append(dice_col.pop())
        dice_col.append(dice_row.pop(0))
        # ex) [1,3,6] , [2,1,5,4]
    # 위로 굴렸을 때 
    if dx[dt] < 0 :
        dice_col.append(dice_col.pop(0))
        dice_row[1] = dice_col[1]
    if dx[dt] > 0 :
        dice_col.insert(0,dice_col.pop())
        dice_row[1] = dice_col[1]
    print(dice_row, dice_col)
roll(1)
roll(2)
roll(3)
roll(4)

# board[X][Y] = 0 
# while commands :
#     dt = commands.pop(0)
#     X,Y = X+dx[dt-1], Y+dy[dt-1]
#     if X >= N or X < 0 or Y < 0 or Y >= M :
#         continue
#     roll(dt) 
#     if board[X][Y] != 0 :
#         dice_col[3] = board[X][Y] 
#         board[X][Y] = 0
#     else :
#         board[X][Y] = dice_col[3]
#     print(dice_col[1])

