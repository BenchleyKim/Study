import sys
import collections
sys.stdin = open("./Algorithm_Study/BOJ/BOJ7576", "r")

M, N = map(int,sys.stdin.readline().split())
mat = []
for i in range(N) :
  mat.append(list(map(int, sys.stdin.readline().split())))


q = collections.deque()
for i in range(N) :
  for j in range(M) :
    if mat[i][j] == 1 :
      q.append((i,j))
queue = collections.deque([q])
check = [[0]*M for i in range(N)]
dx = [0 , 0 ,-1 ,1]
dy = [1 , -1 ,0 ,0]
count = 0

while queue :
  mq = queue.popleft()
  count += 1
  nq = collections.deque()
  while mq :
    tmp = mq.popleft()
    if check[tmp[0]][tmp[1]] == 1 :
      continue
    check[tmp[0]][tmp[1]] = 1 
    for i in range(4) :
      nx = tmp[0] + dx[i]
      ny = tmp[1] + dy[i]
      if (nx >= 0 ) and (nx < N) and (ny >= 0) and (ny < M) :
        if mat[nx][ny] == 0 :
          mat[nx][ny] = 1 
          nq.append((nx,ny))
          continue
        elif mat[nx][ny] == 1 :
          continue
  if nq : 
    queue.append(nq)
  # for m in mat :
  #   print(m)
for i in range(N) :
  for j in range(M) :
    if mat[i][j] == 0 :
      print(-1)
      exit()
print(count-1)   

    
    
    

