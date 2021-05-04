import sys
sys.stdin = open(".\Algorithm_Study\BOJ0504\BOJ14939","r")
input = sys.stdin.readline

board = []
for _ in range(10) :
    board.append(list(input().rstrip()))
for b in board :
    print(b)