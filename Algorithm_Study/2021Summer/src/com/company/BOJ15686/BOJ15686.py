import sys
from itertools import combinations
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/company/BOJ15686/BOJ15686.in","r")
input = sys.stdin.readline


N, M = map(int, input().split())
board = []
for i in range(N) :
    board.append(list(map(int, input().split())))
houses = []
chickens = []
for i in range(N) :
    for j in range(N) :
        if board[i][j] == 1 :
            houses.append((i,j))
            continue
        if board[i][j] == 2 :
            chickens.append((i,j))
INF = sys.maxsize
combs = list(combinations(chickens, M))
ans = INF
for comb in combs :
    total_distance = 0
    for house in houses :
        mn = INF
        for chick in comb :
            mn = min(mn, abs(house[0]-chick[0])+abs(house[1]-chick[1]))
        total_distance += mn
    ans = min(total_distance, ans)
print(ans)