import sys
import collections
sys.stdin = open("./Algorithm_Study/BOJ/BOJ7569", "r")

M, N,H = map(int,sys.stdin.readline().split())
box = []
for k in range(H) :
  mat = []
  for i in range(N) :
    mat.append(list(map(int, sys.stdin.readline().split())))
  box.append(mat)


q = collections.deque()
for h in range(H) :
  for i in range(N) :
    for j in range(M) :
      if box[h][i][j] == 1 :
        q.append((h,i,j))
queue = collections.deque([q])
check = [[[0]*M for i in range(N)] for h in range(H)]
dz = [0, 0, 0, 0, -1, 1]
dx = [0, 0,-1 , 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
count = 0

while queue :
  mq = queue.popleft()
  count += 1
  nq = collections.deque()
  while mq :
    tmp = mq.popleft()
    if check[tmp[0]][tmp[1]][tmp[2]] == 1 :
      continue
    check[tmp[0]][tmp[1]][tmp[2]] = 1 
    for i in range(6) :
      nz = tmp[0] + dz[i]
      nx = tmp[1] + dx[i]
      ny = tmp[2] + dy[i]
      if (nx >= 0 ) and (nx < N) and (ny >= 0) and (ny < M) and (nz >= 0) and (nz < H) :
        if box[nz][nx][ny] == 0 :
          box[nz][nx][ny] = 1 
          nq.append((nz,nx,ny))
          continue
        elif box[nz][nx][ny] == 1 :
          continue
  if nq : 
    queue.append(nq)
  # for m in mat :
  #   print(m)
for k in range(H) :
  for i in range(N) :
    for j in range(M) :
      if box[k][i][j] == 0 :
        print(-1)
        exit()
print(count-1)   

    
    
    

