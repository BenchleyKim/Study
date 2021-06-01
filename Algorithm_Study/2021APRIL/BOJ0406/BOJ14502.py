import sys
from itertools import combinations
from collections import deque
import copy

sys.stdin = open("./Algorithm_Study/BOJ0406/BOJ14502", "r")
input = sys.stdin.readline


N, M = map(int, input().split())
board = []
for i in range(N) :
    board.append(list(map(int, input().split())))

virus_start = []
wall_candidate = []
base_check = [[0]*M for _ in range(N)]
for i in range(N) :
    for j in range(M):
        if board[i][j] == 2 :
            virus_start.append((i,j))
        if board[i][j] == 0 :
            wall_candidate.append((i,j))
        if board[i][j] == 1 :
            base_check[i][j] = 1


candidate_list = list(combinations(wall_candidate, 3))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
mx = 0
for candidate in candidate_list :
    w1 ,w2, w3 =candidate
    board[w1[0]][w1[1]] = board[w2[0]][w2[1]] = board[w3[0]][w3[1]] = 1
    stack = deque(virus_start)
    
    # check = copy.deepcopy(base_check)
    # check[w1[0]][w1[1]] = check[w2[0]][w2[1]] = check[w3[0]][w3[1]] = 1
    

    while stack :
        x,y = stack.popleft()
        if board[x][y] == -1:
            continue
        board[x][y] = -1
        for i in range(4) :
            if x+dx[i] < 0 or x+dx[i] >= N or y+dy[i] < 0 or y+dy[i] >= M :
                continue
            if board[x+dx[i]][y+dy[i]] == 1 :
                continue
            nx, ny = x+dx[i], y+dy[i]
            stack.append((nx,ny))
    cnt = 0
    for i in range(N) :
        for j in range(M) :
            if board[i][j] == 0 :
                cnt+=1 
            if board[i][j] == -1 :
                board[i][j] = 0
    
    board[w1[0]][w1[1]] = board[w2[0]][w2[1]] = board[w3[0]][w3[1]] = 0

    mx = max(mx, cnt)

print(mx)





