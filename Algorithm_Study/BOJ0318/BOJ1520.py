import sys
sys.stdin = open("./Algorithm_Study/BOJ0318/BOJ1520", "r")
input = sys.stdin.readline
M, N = map(int, input().split() )
table = []
for i in range(M) :
  table.append(list(map(int,input().split())))
for t in table :
  print(t)
DP = [[0]* N for i in range(M)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
stack  = [(0,0,1)]
while stack :
  cx, cy,w = stack.pop()
  print(cx,cy,w)
  DP[cx][cy] += w
  for i in range(4) :
    nx , ny = cx+dx[i], cy+dy[i]
    if nx < 0 or nx >= M or ny < 0 or ny >= N :
      continue
    if table[nx][ny] < table[cx][cy] :
      stack.append([nx,ny,DP[cx][cy]])
for d in DP :
  print(d)
print(DP[M-1][N-1])


    

