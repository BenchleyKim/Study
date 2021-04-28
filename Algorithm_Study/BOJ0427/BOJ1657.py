import sys 
sys.stdin = open(".\Algorithm_Study\BOJ0427\BOJ1657","r")
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for i in range(N) :
    board.append(list(map(int, input().split()))))