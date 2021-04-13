import sys
sys.stdin = open("./Algorithm_Study/BOJ0413/BOJ17779","r")
input = sys.stdin.readline

N = int(input())
board = [ ]
for i in range(N) :
    board.append(list(map(int, input().split())))

all_case = []
for d1 in range(1,N) :
    for d2 in range(1,N) :
        for x in range(N) :
            for y in range(N) :
                if x< N-d1-d2  and d1 <= y and y < N-d2  :
                    all_case.append((d1,d2,x,y))
total_sum = 0
for i in range(N) :
    for j in range(N) :
        total_sum += board[i][j]
# print(all_case)
mn = sys.maxsize
for case in all_case :
    d1, d2 ,x ,y = case 
    check = [[0]*N for _ in range(N)]
    arr = [0,0,0,0,0]
    for i in range(N) :
        for j in range(N) : 
            if i < x :
                if j <= y :
                    arr[0] += board[i][j]
                else :
                    arr[1] += board[i][j]
            elif x+d1+d2 < i :
                if j < y+d2-d1 :
                    arr[2] += board[i][j]
                else :
                    arr[3] += board[i][j]
            else :
                
                if i < x+d1 :
                    if j < y-(i-x) :
                        arr[0] += board[i][j]
                else :
                    if  j < y-d1+(i-x-d1) :
                        arr[2] += board[i][j]
                if i <= x+d2 :
                    if j > y+(i-x) :
                        arr[1] += board[i][j]
                else :
                    if j > y+d2-(i-x-d2) :
                        arr[3] += board[i][j]
    
    arr[4] = total_sum - sum(arr)
    
    mn = min(mn, max(arr)-min(arr))
print(mn)
 
        



