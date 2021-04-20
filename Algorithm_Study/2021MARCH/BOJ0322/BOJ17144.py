import sys
sys.stdin = open("./Algorithm_Study/BOJ0322/BOJ17144", "r")
input = sys.stdin.readline

R, C, T = map(int, input().split())
ROOM = []
for i in range(R) :
  ROOM.append(list(map(int,input().split())))
dust = []
airCleaner = []
for i in range(R) :
  for j in range(C) :
    if ROOM[i][j] == -1 :
      airCleaner.append([i,j])
      continue
    if ROOM[i][j] != 0 :
      dust.append([i,j,ROOM[i][j]])

dx = [0,0,1,-1]
dy = [1,-1,0,0]
for t in range(T) :
  nextRoom = [[0]*C for _ in range(R)]
  for d in dust :
    x, y, w = d 
    cnt = 0
    diffusion = []
    for k in range(4) :
      nx ,ny= x+dx[k] , y+dy[k]
      if nx < 0 or nx >= R or ny < 0 or ny >= C or ROOM[nx][ny] == -1:
        continue
      cnt += 1
      diffusion.append([nx,ny])
    nextRoom[x][y] += ROOM[x][y] - ((ROOM[x][y] //5) * cnt)
    for diff in diffusion :
      nx, ny = diff
      nextRoom[nx][ny] += (ROOM[x][y] //5)
  ROOM = nextRoom
  
  x,y =airCleaner[0]
  ROOM[x][y] = -1
  prev_state = 0
  for i in range(1,C) :
    ROOM[x][i] , prev_state=  prev_state, ROOM[x][i]
  for i in range(x-1,-1,-1) :
    ROOM[i][C-1] , prev_state = prev_state , ROOM[i][C-1]
  for i in range(C-2,-1,-1) :
    ROOM[0][i], prev_state = prev_state, ROOM[0][i]
  for i in range(1, x) :
    ROOM[i][0], prev_state = prev_state, ROOM[i][0]
  x,y =airCleaner[1]
  ROOM[x][y] = -1
  prev_state = 0
  for i in range(1,C) :
    ROOM[x][i], prev_state = prev_state, ROOM[x][i]
  for i in range(x+1,R) :
    ROOM[i][C-1], prev_state = prev_state, ROOM[i][C-1]
  for i in range(C-2,-1,-1) :
    ROOM[R-1][i], prev_state = prev_state, ROOM[R-1][i]
  for i in range(R-2, x,-1) :
    ROOM[i][0], prev_state = prev_state, ROOM[i][0]
  dust = []
  for i in range(R) :
    for j in range(C) :
      if ROOM[i][j] == -1 :
        continue
      if ROOM[i][j] != 0 :
        dust.append([i,j,ROOM[i][j]])

  # print(t+1)
  # for r in ROOM :
  #   print(r)
  
ans = 0
for i in range(R) :
  for j in range(C) :
    if ROOM[i][j] != -1 :
      ans += ROOM[i][j]
print(ans)


  
       


