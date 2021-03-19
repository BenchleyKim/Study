import sys
import collections
import heapq
sys.stdin = open("./Algorithm_Study/BOJ0319/BOJ1504", "r")
input = sys.stdin.readline

N, E = map(int, input().split())
graph = {i : {} for i in range(1,N+1)} 
for _ in range(E) :
  a, b, c =map(int, input().split())
  graph[a][b] = c 
  graph[b][a] = c 
v1, v2 = map(int, input().split())
INF = sys.maxsize

def dijkstra(graph, s):
  distance = [INF] * (N+1)
  check  = [0] * (N+1)
  stack = []
  heapq.heappush(stack, (0,s))
  while stack :
    w, tmp = heapq.heappop(stack)
    if distance[tmp] > w :
      distance[tmp] = w 
      check[tmp] = 0
    if check[tmp] : 
      continue
    check[tmp] = 1
    subnodes = graph[tmp].keys()
    for node in subnodes :
        heapq.heappush(stack, (distance[tmp]+ graph[tmp][node],node))
  return distance
results = [ ]
for i in [1,v1,v2]:
  result = dijkstra(graph, i)
  results.append(result)


ans = min(results[0][v1] + results[1][v2] + results[2][N],results[0][v2] + results[2][v1] + results[1][N] )
if ans >= INF :
  print(-1)
else :
  print(ans)