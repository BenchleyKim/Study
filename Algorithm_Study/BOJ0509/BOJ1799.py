import sys
sys.stdin = open(".\Algorithm_Study\BOJ0509\BOJ1799","r")
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

arr = []

for i in range(N) :
    for j in range(N) :
        if board[i][j] == 1 :
            arr.append((i,j))
check = [0] * len(arr)
mx = 0 
print(arr)
def backtracking(i, check ) :
    global mx 
    print(i,check,mx)
    if i == len(arr) :
        mx = max(mx, check.count(1))
        return
    if check[i] :
        base = check[i]
        backtracking(i+1, check)
        check[i] = base
    else :
        check[i] = 1
        for j in range(len(arr)) :
            if i == j :
                continue
            if abs(arr[i][0]-arr[j][0]) == abs(arr[i][1]-arr[j][1]) :
                check[j] = -1      
        backtracking(i+1, check)
        check[i] = 0
        backtracking(i+1, check)
backtracking(0, check)
print(mx)
