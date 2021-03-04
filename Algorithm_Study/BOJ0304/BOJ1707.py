import sys 
sys.stdin = open("./Algorithm_Study/BOJ0304/BOJ1707", "r")

# 싸이클이 있는지 확인하는 게 관건
K = int(sys.stdin.readline())
for _ in range(K) :
  V, E = map(int ,sys.stdin.readline().split())
  graph = {}
  for i in range(E) :
    start, end = map(int ,sys.stdin.readline().split())
    if start in graph.keys() :
      graph[start].append(end)
    else :
      graph[start] = [end]
    if end in graph.keys() :
      graph[end].append(start)
    else :
      graph[end] = [start]
  print(graph)
