import sys
sys.stdin = open("./Algorithm_Study/BOJ0414/BOJ2098","r")
input = sys.stdin.readline

N = int(input())
board = []
for i in range(N) :
    board.append(list(map(int, input().split())))
for b in board :
    print(b)
graph = { i : {} for i in range(1,N+1)}
for i in range(N) :
    for j in range(N) :
        if board[i][j] :
            graph[i+1][j+1] = board[i][j]
