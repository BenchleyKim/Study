import sys 
from itertools import combinations
sys.stdin = open("./Algorithm_Study/STD0403/sstt04", "r")
input = sys.stdin.readline

N = int(input())
board = []
for i in range(N) :
    board.append(list(map(int, input().split())))

player_list = list(range(1,N+1))
all_cases = list(combinations(player_list,N//2))
mn = sys.maxsize
print(mn)
for case in all_cases :
    Ateam = 0
    Bteam = 0
    for i in range(1,N+1) :
        if i in case :
            for member in case :
                Ateam += board[i-1][member-1]
        else :
            for member in range(1,N+1) :
                if member not in case :
                    Bteam += board[i-1][member-1]
    mn = min(mn, abs(Ateam-Bteam))
            
print(mn)
