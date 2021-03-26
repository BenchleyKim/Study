import sys
import copy
sys.stdin = open("./Algorithm_Study/BOJ0326/BOJ13460", "r")
input = sys.stdin.readline
N, M =  map(int, input().split())
board =[ ]
for _ in range(N) :
  board.append(list(input().rstrip()))
# 왼쪽으로 기울이기 , 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기
actions = [0,1,2,3]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
R = []
B = []
O = []
for i in range(N) :
  for j in range(M) :
    col = board[i][j] 
    if col == 'R' :
      R = [i, j]
      board[i][j] = '.'
    if col == 'B' :
      B = [i, j]
      board[i][j] = '.'
    if col == 'O' :
      O = [i, j]
queue = [[R,B,0]]
endflag = False


while queue :
  tR, tB ,count = queue.pop(0)
  # print(tR,tB,count)
  if endflag :
    print(count)
    break
  if count > 10 :
    print(-1) 
    break
  endflag = False
  for action in actions :
    nR = [tR[0], tR[1]]
    nB = [tB[0], tB[1]]
    flag  = False
    if board[nR[0] + dx[action]][nR[1] + dy[action]] == '#' and board[nB[0] + dx[action]][nB[1] + dy[action]] == '#' :
      continue
    # R의 막다른 곳 찾기
    while board[nR[0] + dx[action]][nR[1] + dy[action]] == '.' or board[nR[0] + dx[action]][nR[1] + dy[action]] == 'O' :
      if nR[0] == tB[0] and nR[1] == tB[1] :
      # 진행방향쪽에 B가 있는 경우 
        flag = True      
      if board[nR[0]][nR[1]] == 'O' :
        endflag = True
        
      nR = [nR[0] + dx[action], nR[1] + dy[action]]
    if flag or board[nR[0]][nR[1]] == '#' :
      nR = [nR[0] - dx[action], nR[1] - dy[action]]
    flag = False
    while board[nB[0] + dx[action]][nB[1] + dy[action]] == '.' or board[nB[0] + dx[action]][nB[1] + dy[action]] == 'O' :
      if nB[0] == tR[0] and nB[1] == tR[1] :
      # 진행방향쪽에 R이 있는 경우 
        flag = True      
      if board[nB[0]][nB[1]] == 'O' :
        endflag = False
        
      nB = [nB[0] + dx[action], nB[1] + dy[action]]
    if endflag :
      continue
    if flag or  board[nB[0]][nB[1]] == '#' : 
      nB = [nB[0] - dx[action], nB[1] - dy[action]]
    queue.append([nR,nB,count+1])






