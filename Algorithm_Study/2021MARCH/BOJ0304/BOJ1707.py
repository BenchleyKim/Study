import sys 
from collections import deque
sys.stdin = open("./Algorithm_Study/BOJ0304/BOJ1707", "r")




# 싸이클이 있는지 확인하는 게 관건
K = int(sys.stdin.readline())
for _ in range(K) :
  V, E = map(int ,sys.stdin.readline().split())
  graph = {i : [] for i in range(1,V+1)}
  check = [0] * (V+1)
  for i in range(E) :
    start, end = map(int ,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)
    
  check = [0] * (V+1)
  color = [0] * (V+1)
  
  glist = graph.keys()
  flag = True
  Finished = True
  controlQ = deque([1])
  while controlQ :
    root = controlQ.pop()
    queue = deque([root])
    color[root] = 1
    while queue :
      tmp = queue.popleft()
      check[tmp] = 1
      for j in graph[tmp] :
        if check[j] == 0 :
          check[j] = 1 
          color[j] = -(color[tmp])
          queue.append(j)
        elif color[j] == color[tmp] :
          flag = False
          break
      if flag == False :
        break
    if flag == False :
      break
    for i in range(root,V+1) :
      if check[i] == 0 :
        controlQ.append(i)
        Finished = False
        break
    if Finished :
      break
  if flag == False :
    print("NO")
    continue
  print("YES")
        

 
  