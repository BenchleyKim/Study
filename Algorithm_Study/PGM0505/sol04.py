import sys

def solution(board):
    N = len(board) 
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    straigt = 100
    corner = 500
    INF = sys.maxsize
    check = [[INF]*N for _ in range(N)]
    
    stack = [(0,0,0),(0,0,2)]
    check[0][0] = 0
    while stack :
        cx, cy, direct = stack.pop()
        for d in range(4) :
            nx, ny = cx+dx[d], cy+dy[d] 
            if 0<= nx < N and 0<= ny < N :
                if board[nx][ny] == 1 :
                    continue
                if d == direct :
                    if check[nx][ny] >= check[cx][cy] + straigt :
                        check[nx][ny] = check[cx][cy] + straigt
                        stack.append((nx,ny,d))
                else :
                    if check[nx][ny] >= check[cx][cy] + corner + straigt :
                        check[nx][ny] = check[cx][cy] + corner + straigt
                        stack.append((nx,ny,d))
    answer = check[N-1][N-1]
    return answer







print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))