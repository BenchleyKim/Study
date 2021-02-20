import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ1260", "r")

N, M , V = map(int, input().split())
D = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M) :
  a, b = map(int, input().split())
  D[a][b] = 1
  D[b][a] = 1 
check = [0] *(N+1)
stack = [V]

while stack:
  node = stack.pop()
  if check[node] :
    continue
  check[node] = 1
  print(node, end=' ') 
  for i in range(N,0,-1) :
    if D[node][i] :
      stack.append(i)
print()
check = [0] *(N+1)
stack = [V]
while stack:
  node = stack.pop(0)
  if check[node] :
    continue
  check[node] = 1
  print(node, end=' ') 
  for i in range(1,N+1) :
    if D[node][i] :
      stack.append(i)





