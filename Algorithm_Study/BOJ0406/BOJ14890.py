import sys
sys.stdin = open("./Algorithm_Study/BOJ0406/BOJ14890", "r")
input = sys.stdin.readline

N , L = map(int, input().split())
board = [ ]
for i in range(N) :
    board.append(list(map(int, input().split())))

for b in board :
    print(b)
ans = 0
check = [[0]*N for _ in range(N)]


for i in range(N) :
    check = [0] * M
    for j in range(N) :
        





    
