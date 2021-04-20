

n = int(input())
k = int(input())
edges = {}
for i in range(k):
  a,b,w = list(map(int, input().split()))
  if a not in edges.keys() :
    edges[a] = {b:w}
  if b not in edges.keys() :
    edges[b] = {a:w}
  edges[a][b] = w 
  edges[b][a] = w 

visited = [0] * (n+1)
for i in edges.keys():
  if not visited[i] :
    print(" ") 
    visited[i] = 1
  print(i, end=' ')
  for j in edges[i].keys():
    print(end=' -> ')
    print(j, end = ' Data : ')
    print(edges[i][j], end= ' ')


# DFS 스택 
print("DFS")
visited = [0] * (n+1)
stack = []
stack.append(1)
visited[1] = 1
while True :
  if len(stack) == 0 :
    break
  root = stack.pop()
  sort = sorted(list(edges[root].keys()))
  for i in sort :
    if not visited[i]: print(i);stack.append(i);visited[i]=1; break


# DFS 재귀 
print("DFS")
visited = [0] * (n+1)
def dfs(root):
  if visited[root]:return
  visited[root] = 1
  print(root)
  
  sort = sorted(list(edges[root].keys()))
  for i in sort:
    dfs(i)

dfs(1)


# BFS 
print("BFS")
visited = [0] * (n+1)
queue = []
queue.append(1)
while True:
  if len(queue) == 0:
    break
  r = queue.pop(0)
  if visited[r] :
    continue
  visited[r] = 1
  print(r)
  sort = sorted(list(edges[r].keys()))
  queue.extend(sort)
  








