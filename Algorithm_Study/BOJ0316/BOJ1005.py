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
  result = { i+1 : 0 for i in range(N)}
  for i in check.keys() :
    if check[i] == 0 :
      stack.append(i)
      result[i] = arr[i-1]

  while stack :
    tmp = stack.pop()
    for k in graph[tmp] :
      check[k] -= 1
      if result[k] != 0:
        result[k] = max(result[k], result[tmp] + arr[k-1])
      else :
        result[k] = result[tmp] + arr[k-1]
      if check[k] == 0 :
        stack.append(k)
  target = int(sys.stdin.readline())
  print(result[target])


