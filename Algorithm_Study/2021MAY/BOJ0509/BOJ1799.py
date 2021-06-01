import sys
sys.stdin = open(".\Algorithm_Study\BOJ0509\BOJ1799","r")
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

larr = []
rarr = []
for i in range(N) :
    for j in range(N) :
        if board[i][j] == 1 :
            if i+j % 2 :
                larr.append((i,j))
            else :
                rarr.append((i,j))
mx = 0 
print(larr)
print(rarr)

def backtracking(i, check ) :
    global mx 
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


check = [0] * len(larr)
arr = larr
backtracking(0, check)
print(mx)
ans = mx

mx = 0
arr = rarr 
check = [0] * len(rarr)
backtracking(0, check)
ans += mx
print(mx)
print(ans)


##############

n=int(input())

chess_map=[]
black=[]
white=[]
color=[[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        color[i][j]=(i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)

for i in range(n):
    chess_map.append(list(map(int, input().split())))
    for j in range(n):
        # True가 검은색
        if chess_map[i][j]==1 and color[i][j]==1:
            black.append((i,j))
        # False가 흰색
        if chess_map[i][j]==1 and color[i][j]==0:
            white.append((i,j))

# 검은색인 경우
Bcnt=0
# 흰색인 경우
Wcnt=0

isused01=[0]*(n*2-1)
isused02=[0]*(n*2-1)

def fun(bishop,index,count):
    global Bcnt, Wcnt
    if index==len(bishop):
        rx,ry=bishop[index-1]
        # 블랙이면 Bcnt 최대값
        if color[rx][ry]:
            Bcnt=max(Bcnt,count)
        # 흰색이면 Wcnt 최대값
        else:
            Wcnt=max(Wcnt,count)
        return

    x,y=bishop[index]
    if isused01[x+y] or isused02[x-y+n-1]:
        fun(bishop,index+1,count)
    else:
        isused01[x+y]=1
        isused02[x-y+n-1]=1
        fun(bishop,index+1,count+1)
        isused01[x+y]=0
        isused02[x-y+n-1]=0
        fun(bishop,index+1,count)

if len(black)>0:
    fun(black,0,0)
if len(white)>0:
    fun(white,0,0)
print(Bcnt+Wcnt)