import sys
sys.stdin = open("./Algorithm_Study/BOJ0313/BOJ2206", "r")

N , M = map(int , sys.stdin.readline().split())
MAP = [[0]*M for _ in range(N)]

for i in range(N) :
  line = sys.stdin.readline()
  for j in range(M) :
    MAP[i][j] = int(line[j])

print(MAP)
check = [[0]*M for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
queue = [(0,0,0)]
while queue : 
  X,Y,W = queue.pop(0)
  if X == N-1 and Y == M-1 :
    print(W+1)
    break
  if check[X][Y]:
    continue
  print(X,Y)
  check[X][Y] = W+1
  for i in range(4) :
    if X+dx[i] < 0 or X+dx[i] > N-1 or Y+dy[i] < 0 or Y+dy[i] > M-1 :
      continue
    if MAP[X+dx[i]][Y+dx[i]] == 1 :
      continue
    queue.append([X+dx[i],Y+dy[i],check[X][Y]])




