import sys
import copy
sys.stdin = open("./Algorithm_Study/BOJ0324/BOJ12100", "r")
input = sys.stdin.readline
N = int(input())
B = []
for _ in range(N) :
  B.append(list(map(int, input().split())))

# 상하좌우
actions = [0,1,2,3]
ix = [(0,N,1),(N-1,-1,-1),(0,N,1),(0,N,1)]
iy = [(0,N,1),(0,N,1),(0,N,1),(N-1,-1,-1)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def game(board, count, action) :
  global mx
  count += 1
  check = [[0]* N for _ in range(N)]
  for i in range(ix[action][0],ix[action][1],ix[action][2]) :
    for j in range(iy[action][0],iy[action][1],iy[action][2]) :
      if board[i][j] == 0 :
        continue
      nx, ny = i+dx[action], j+dy[action]
      if nx < 0 or nx >= N or ny < 0 or ny >= N :
        continue
      while nx +dx[action] >= 0 and nx +dx[action] < N and ny +dy[action] >= 0 and ny+dy[action] < N :
        if board[nx][ny] == 0 :
          nx += dx[action]
          ny += dy[action]
          continue
        else :
          break 
      if board[i][j] == board[nx][ny] and check[nx][ny] == 0 :
        board[nx][ny] += board[i][j]
        board[i][j] = 0
        check[nx][ny] = 1
      else :
        if board[nx][ny] == 0 :
          board[nx][ny],board[i][j] = board[i][j],0
        else :
          if nx-dx[action]==i and ny-dy[action] == j :
            continue
          board[nx-dx[action]][ny-dy[action]], board[i][j] = board[i][j] , 0
  for i in range(N) :
    for j in range(N) :
      mx = max(board[i][j], mx)
  if count == 5 :
    return
  for i in range(4) :
    new_board = copy.deepcopy(board)
    game(new_board,count,i)

mx = 0
for i in range(4) :
  new_B = copy.deepcopy(B)
  game(new_B,0,i)
print(mx)
          

