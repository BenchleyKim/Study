import sys 
import heapq
sys.stdin = open("./Algorithm_Study/BOJ0401/BOJ17472", "r")
input = sys.stdin.readline
N, M = map(int, input().split())
MAP = [ ]
for i in range(N) :
  MAP.append(list(map(int,input().split())))
queue = []
for i in range(N) :
  for j in range(M) : 
    if MAP[i][j] == 1 :
      queue.append((i,j))

visited_check = [[0]*M for _ in range(N)]
count = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
# box_size = [왼쪽 위 , 오른쪽 아래]
box_size = {}
for node in queue :
  sx, sy = node 
  if visited_check[sx][sy] :
    continue
  count += 1
  stack = [(sx,sy)]
  # print(count)
  while stack :
    tx,ty = stack.pop()
    if visited_check[tx][ty] :
      continue
    visited_check[tx][ty] = 1
    MAP[tx][ty] = count
    if count in box_size.keys() :
      box_size[count][0][0] = min(tx,box_size[count][0][0])
      box_size[count][0][1] = min(ty,box_size[count][0][1])
      box_size[count][1][0] = max(tx,box_size[count][1][0])
      box_size[count][1][1] = max(ty,box_size[count][1][1])
    else :
      box_size[count] = [[tx,ty],[tx,ty]]
    for d in range(4):
      nx , ny = tx+dx[d] , ty+dy[d]
      if nx < 0 or nx >= N or ny < 0 or ny >= M :
        continue
      if MAP[nx][ny] == 1 :
        if visited_check[nx][ny] :
          continue
        stack.append((nx,ny))
graph = {i:{} for i in range(1,count+1)}
for i in range(N) :
  for j in range(M) :
    if MAP[i][j] == 0 :
      continue
    for d in range(4) :
      nx,ny = i+dx[d], j+dy[d] 
      length = 1
      if nx < 0 or nx >= N or ny < 0 or ny >= M :
        continue
      if MAP[nx][ny] == MAP[i][j] :
        continue
      while True :
        nx, ny = nx+dx[d], ny+dy[d]
        length += 1
        if nx < 0 or nx >= N or ny < 0 or ny >= M :
          break
        if MAP[nx][ny] == MAP[i][j] :
          break
        if MAP[i][j] != MAP[nx][ny] and MAP[nx][ny] != 0 :
          if length > 2 :
            if MAP[nx][ny] in graph[MAP[i][j]].keys() :
              graph[MAP[i][j]][MAP[nx][ny]] = min(length-1,graph[MAP[i][j]][MAP[nx][ny]])
            else :
              graph[MAP[i][j]][MAP[nx][ny]] = length-1
          break

heap = []
heapq.heappush(heap,(0,1))
ans = 0
check = [0] * (count+1)
while heap :
  l,node = heapq.heappop(heap)
  if check[node] :
    continue
  check[node] = 1
  ans += l
  for sub in graph[node].keys():
    heapq.heappush(heap, (graph[node][sub],sub))
for i in range(1,count+1) :
  if check[i] == 0 :
    print(-1)
    sys.exit()
    break
print(ans)