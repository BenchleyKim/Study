import sys 
sys.stdin = open("./Algorithm_Study/STD0418/test01", "r")
input = sys.stdin.readline

N, M = map(int , input().split())
board = [ ]
for i in range(N ) :
    board.append(list(input().rstrip()))
# print(board)
white_board = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']] * 4 
black_board = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']] * 4

mn = sys.maxsize
for i in range(N-7) : 
    for j in range(M-7) :
        cnt = 0

        for x in range(8) :
            for y in range(8) :
                if board[i+x][j+y] != white_board[x][y] :
                    cnt += 1
        mn = min(mn, cnt)
        cnt = 0

        for x in range(8) :
            for y in range(8) :
                if board[i+x][j+y] != black_board[x][y] :
                    cnt += 1
        mn = min(mn, cnt)
print(mn)

