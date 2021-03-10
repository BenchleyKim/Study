import sys 
sys.stdin = open("./Algorithm_Study/BOJ0310/BOJ1865", "r")

read = sys.stdin.readline
INF = sys.maxsize
TC = int(read())
for _ in range(TC) :
  N , M , W= map(int, read().split())
  graph = {i+1:{} for i in range(N)}
  for i in range(M) :
    S , E, T = map(int, read().split())
    if E in graph[S].keys() :
      graph[S][E] = min(graph[S][E],T)
    else : graph[S][E] = T
    if S in graph[E].keys() :
      graph[E][S] = min(graph[E][S],T)
    else : graph[E][S] = T
  for i in range(W) :
    S , E, T = map(int, read().split())
    graph[S][E] = -T
  result = [INF for _ in range(N+1)]
  result[1] = 0
  for _ in range(2*M+W) :
    for node in graph.keys() :
      for sub in graph[node].keys() :
        if result[sub] > result[node] + graph[node][sub] : 
          result[sub] = result[node] + graph[node][sub]
  Flag = False
  for node in graph.keys() :
    if Flag : break
    for sub in graph[node].keys() :
      if result[sub] > result[node] + graph[node][sub] :
        Flag = True
        break
  if Flag : print("YES")
  else : print("NO")
      
      


