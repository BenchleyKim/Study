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
      airCleanera.append([i,j])
      
      continue
    if ROOM[i][j] != 0 :
      dust.append([i,j,ROOM[i][j]])
    if 

cycle = [dust]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for t in range(T) :
  next_dust = []
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
    for diff in diffusion :
      nx, ny = diff
      next_dust.append([nx,ny,d])
       

print(dust)
for r in ROOM :
  print(r)
