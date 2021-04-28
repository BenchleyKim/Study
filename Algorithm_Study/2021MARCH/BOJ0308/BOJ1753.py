import sys 
import heapq
sys.stdin = open("./Algorithm_Study/BOJ0308/BOJ1753", "r")
MAX = sys.maxsize
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = {i : {}for i in range(1,V+1)}
for i in range(E) :
  u,v,w = map(int, sys.stdin.readline().split())
  if graph[u].get(v) != None:
    if graph[u][v] < w :
      continue
  graph[u][v] = w
      

queue = []
heapq.heappush(queue, (0,K))
check = [MAX] * (V+1)
while queue :
  weight, tmp= heapq.heappop(queue)
  if check[tmp] <= weight :
    continue
  # print(tmp, weight)
  check[tmp] = weight
  for k, w in graph[tmp].items() :
    heapq.heappush(queue, (check[tmp] + w, k))
for i in range(1,V+1) :
  if check[i] == MAX :
    print("INF")
    continue
  print(check[i])