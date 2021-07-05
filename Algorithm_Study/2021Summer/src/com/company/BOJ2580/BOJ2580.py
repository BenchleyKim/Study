import sys
from itertools import combinations
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/company/BOJ2580/BOJ2580.in","r")
input = sys.stdin.readline

board = [list(map(int, input().split())) for i in range(9)]
base_range = set(range(1,10))

def find_candi(i, j) :
    base_range = set(range(1,10))
    for x in range(9) :
        base_range.discard(board[x][j])
    for y in range(9) :
        base_range.discard(board[i][y])
    for bx in range((i//3)* 3 ,(i//3)* 3 + 3 ) :
        for by in range((j//3)* 3 ,(j//3)* 3 +3 ) :
            base_range.discard(board[bx][by])
    return base_range

queue = []
for i in range(9) :
    for j in range(9) :
        if board[i][j] == 0 :
            queue.append((i,j))
def dfs(idx) :
    if idx == len(queue) :
        for b in board :
            print(*b)
        sys.exit()
    i,j = queue[idx]
    available_range = list(find_candi(i,j))
    for can in available_range :
        board[i][j] = can
        dfs(idx+1)
        board[i][j] = 0
dfs(0)
        