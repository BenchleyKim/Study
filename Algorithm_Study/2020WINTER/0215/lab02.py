import sys 
sys.stdin = open("./Algorithm_Study/0215/lab02", "r")
N , M = list(map(int, input().split()))
tmap = [list(map(int,input())) for _ in range(N)]
# for m in tmap :
#   print(m)
queue = []
check = [[0]*M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0
for i in range(N) :
  for j in range(M) :
    if tmap[i][j] == 1 :
      if check[i][j] == 1 :
        continue
      check[i][j] = 1
      count += 1
      queue.append([i,j])
      while len(queue) != 0 :
        x ,y = queue.pop(0)
        # print(j,i, x,y,count)
        for d in range(4) :
          nx = x + dx[d]
          ny = y + dy[d]
          if 0 > nx or nx >= N: continue
          if 0 > ny or ny >= M: continue
          if tmap[nx][ny] == 0: continue
          if check[nx][ny] != 0: continue
          check[nx][ny] = 1
          queue.append([nx,ny])
print(count)
