import sys
sys.stdin = open("./Algorithm_Study/BOJ0323/BOJ2252", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
graph = { i : [] for i in range(1,N+1)}
check = { i : 0 for i in range(1,N+1)}

for _ in range(M) :
  A, B = map(int, input().split())
  graph[A].append(B)
  check[B] += 1

stack = []
for i in range(1,N+1) :
  if check[i] == 0 :
    stack.append(i)
while stack : 
  tmp = stack.pop()
  print(tmp, end=' ') 
  for i in graph[tmp] :
    check[i] -= 1
    if check[i] == 0:
      stack.append(i)


