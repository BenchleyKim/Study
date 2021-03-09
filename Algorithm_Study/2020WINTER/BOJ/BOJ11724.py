import sys 
import collections
sys.stdin = open("./Algorithm_Study/BOJ/BOJ11724", "r")

N, M = map(int, sys.stdin.readline().split())
graph = {}
nodes = collections.deque()
for _ in range(M) :
  S, E = map(int, sys.stdin.readline().split())
  nodes.append(S)
  if S in graph.keys() :
    graph[S].append(E)
  else :
    graph[S] = [E]
  if E in graph.keys() :
    graph[E].append(S)
  else :
    graph[E] = [S]

check = [0] * (N+1)
count = 0
vcount = 0 
for node in nodes :
  if check[node] == 1 :
    continue
  count += 1
  stack = [node]
  while stack :
    tmp = stack.pop()
    if check[tmp] == 1 :
      continue
    check[tmp] = 1
    vcount += 1 
    stack.extend(graph[tmp])

print(count+N-vcount)
