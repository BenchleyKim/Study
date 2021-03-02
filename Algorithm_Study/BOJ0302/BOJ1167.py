import sys 
sys.stdin = open("./Algorithm_Study/BOJ0302/BOJ1167", "r")

V = int(sys.stdin.readline())
graph = {}
for _ in range(V) :
  S = list(map(int,sys.stdin.readline().split()))
  start = S.pop(0)
  graph[start] = {}
  for i in range((len(S)-1)//2) :
    end , weight  = S[2*i], S[2*i+1]
    graph[start][end] = weight

print(graph)
check = [0] * (V+1)
stack  = [1]
D = 0 
while stack :
  node = stack.pop()
  print("tmp : ", node)
  if check[node] :
    continue
  check[node] = 1
  print(node)
  vlist = graph[node].keys()
  stack.extend(vlist)


    
  

