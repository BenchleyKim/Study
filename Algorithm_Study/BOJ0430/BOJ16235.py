import sys 
import heapq
sys.stdin = open("./Algorithm_Study/BOJ0430/BOJ16235","r")
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [[5]*N for _ in range(N)]
arr = []
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
for i in range(N) :
    arr.append(list(map(int,input().split())))
tree = []
for i in range(M) :
    x,y,z = map(int,input().split())
    x -= 1
    y -= 1
    heapq.heappush(tree, (z,x,y))
while K > 0 :
    print(K)
    K -= 1
    ntree = []
    dtree = []
    while tree :
        z,x,y = heapq.heappop(tree)
        if board[x][y] >= z :
            board[x][y] -= z
            z+=1
            if z % 5 == 0 :
                for d in range(8) :
                    nx, ny=  x+dx[d], y+dy[d]
                    if 0<= nx < N and 0<= ny < N:
                        heapq.heappush(ntree,(1,nx,ny))
            heapq.heappush(ntree,(z,x,y))
        else :
            dtree.append((z,x,y))
    for node in dtree :
        z,x,y = node
        board[x][y] += z//2 
    for i in range(N) :
        for j in range(N) :
            board[i][j] += arr[i][j]
    tree = ntree
print(len(tree))
    
