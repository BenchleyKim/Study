import sys 
sys.stdin = open("./Algorithm_Study/BOJ0304/BOJ1707", "r")

K = int(sys.stdin.readline())
for _ in range(K) :
  V, E = map(int ,sys.stdin.readline().split())
  graph = [[0] * (V+1) for _ in range(V+1)]
  for i in range(E) :
    start, end = map(int ,sys.stdin.readline().split())
    graph[start][end] = 1
    graph[end][start] = 1
  for g in graph: 
    print(g)
    