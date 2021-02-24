import sys
sys.stdin = open("./Algorithm_Study/BOJ/BOJ7576", "r")

M, N = map(int,sys.stdin.readline().split())
mat = []
for i in range(N) :
  mat.append(list(map(int, sys.stdin.readline().split())))

for m in mat :
  print(m)

queue = []
for i in range(N) :
  for j in range(M) :
    if mat[i][j] == 1 :
      queue.append((i,j))
print(queue)
