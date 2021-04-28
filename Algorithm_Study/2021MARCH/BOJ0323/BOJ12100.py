import sys
sys.stdin = open("./Algorithm_Study/BOJ0323/BOJ12100", "r")
input = sys.stdin.readline
N = int(input())
board = []
for _ in range(N) :
  board.append(list(map(int, input().split())))
# for b in board :
#   print(b)
# print()
actions = [ 0,1,2,3]
###    left , right, up, down
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ix = [(N-1,-1,-1),(0,N,1),(0,N,1),(0,N,1)]
iy = [(0,N,1),(0,N,1),(N-1,-1,-1),(0,N,1)]

def game(board, setCount , action) :
  # board  : 현재의 게임판 
  # setCount : 현재까지 움직인 횟수 
  # action : 동작 
  setCount += 1
  
  nextBoard = [[0] * N for _ in range(N)]
  check = [[0] * N for _ in range(N)]
  mx = 0
  for i in range(ix[(action)%4][0],ix[(action)%4][1],ix[(action)%4][2]) :
    for j in range(iy[(action)%4][0],iy[(action)%4][1],iy[(action)%4][2]) :
      nx , ny= i + dx[action], j + dy[action]
      if nx < 0 or nx >= N or ny < 0 or ny >= N  :
        continue
      if board[nx][ny] == 0 :
        while nx+dx[action] >= 0 and nx+dx[action] < N and ny+dy[action] >= 0 and ny+dy[action] < N :
          if board[nx+dx[action]][ny+dy[action]] != 0 :
            break
          nx, ny = nx + dx[action], ny + dy[action]
        board[nx][ny],board[i][j] = board[i][j], 0
  
  for i in range(ix[action][0],ix[action][1],ix[action][2]) :
    for j in range(iy[action][0],iy[action][1],iy[action][2]) :
      nx , ny= i + dx[action], j + dy[action]
      if nx < 0 or nx >= N or ny < 0 or ny >= N  :
        nextBoard[i][j] = board[i][j]
        continue
      if check[nx][ny] :
        nextBoard[i][j] = board[i][j]
        continue
      if board[nx][ny] == board[i][j] :
        # print(i,j,nx,ny)
        check[i][j] = 1 
        # while nx+dx[action] >= 0 and nx+dx[action] < N and ny+dy[action] >= 0 and ny+dy[action] < N and nextBoard[nx][ny] == 0 :
        #   nx, ny = nx + dx[action], ny + dy[action]
        nextBoard[nx][ny] = board[i][j] * 2
      else : 
        nx , ny = i, j
        # while nx+dx[action] >= 0 and nx+dx[action] < N and ny+dy[action] >= 0 and ny+dy[action] < N and board[nx][ny] == 0 :
        #   nx, ny = nx + dx[action], ny + dy[action]
        # check[i][j] = 1
        nextBoard[nx][ny] = board[i][j]
  # for i in range(ix[(action+1)%4][0],ix[(action+1)%4][1],ix[(action+1)%4][2]) :
  #   for j in range(iy[(action+1)%4][0],iy[(action+1)%4][1],iy[(action+1)%4][2]) :
  #     nx , ny= i + dx[action], j + dy[action]
  #     if nx < 0 or nx >= N or ny < 0 or ny >= N  :
  #       continue
  #     if nextBoard[nx][ny] == 0 :
  #       nextBoard[nx][ny],nextBoard[i][j] = nextBoard[i][j], 0
  board = nextBoard
  for i in range(ix[(action)%4][0],ix[(action)%4][1],ix[(action)%4][2]) :
    for j in range(iy[(action)%4][0],iy[(action)%4][1],iy[(action)%4][2]) :
      nx , ny= i + dx[action], j + dy[action]
      if nx < 0 or nx >= N or ny < 0 or ny >= N  :
        continue
      if board[nx][ny] == 0 :
        while nx+dx[action] >= 0 and nx+dx[action] < N and ny+dy[action] >= 0 and ny+dy[action] < N :
          if board[nx+dx[action]][ny+dy[action]] != 0 :
            break
          nx, ny = nx + dx[action], ny + dy[action]
        board[nx][ny],board[i][j] = board[i][j], 0
  print(setCount, action)
  for b in board :
    print(b)
  mx = 0
  global global_mx
  if setCount == 5 :

    for b in nextBoard :
      mx = max(mx, max(b))
    if global_mx < mx :
      global_mx = mx 
      
    # global_mx = max(mx,global_mx)
    return 
  else : 
    for action in actions :
      game(board,setCount,action)


global_mx = 0
for action in actions :
  game(board,0,action)

print(global_mx)