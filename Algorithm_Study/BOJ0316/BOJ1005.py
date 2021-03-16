import sys
sys.stdin = open("./Algorithm_Study/BOJ0316/BOJ1005", "r")

T = int(sys.stdin.readline())
for _ in range(T) :
  N, K = map(int, sys.stdin.readline().split())
  arr = list(map(int, sys.stdin.readline().split()))
  check = { i+1 : 0 for i in range(N)}
  graph = {i+1:[] for i in range(N)}
  for i in range(K) :
    X, Y = map(int, sys.stdin.readline().split())
    graph[X].append(Y)
    check[Y] += 1
  stack = []
  for i in check.keys() :
    if check[i] == 0 :
      stack.append(i)
  print(stack)
  print(graph)
  while stack :
    tmp = stack.pop()
    for k in graph[tmp] :
      check[k] -= 1
    
  print(check)
  target = int(sys.stdin.readline())


