import sys 
from collections import deque
sys.stdin = open("./Algorithm_Study/BOJ0327/BOJ2623", "r")
input = sys.stdin.readline

N , M = map(int, input().split())
graph = { i:[] for i in range(1,(N+1)) }
check = [0] * (N+1)
for _  in range(M) :
  arr = list(map(int, input().split()))
  for i in range(1,len(arr)-1) :
    graph[arr[i]].append(arr[i+1])
    check[arr[i+1]] += 1
queue = deque()
for i in range(1,N+1) :
  if check[i] == 0:
    queue.append(i)
answer = []
while queue :
  node = queue.popleft()
  answer.append(node)
  for sub in graph[node] :
    check[sub] -= 1
    if check[sub] == 0:
      queue.append(sub)
flag = True
for i in range(1,N+1) :
  if check[i] != 0 :
    flag = False
    break
if flag :
  for ans in answer :
    print(ans)
else : 
  print(0)