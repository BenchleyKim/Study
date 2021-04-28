import sys
sys.stdin = open("./Algorithm_Study/BOJ0421/BOJ20543","r")
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for i in range(N) :
    board.append(list(map(int, input().split())))

for b in board :
    print(b)
