import sys
import heapq 
import collections
sys.stdin = open("./Algorithm_Study/BOJ0320/BOJ2056", "r")
input = sys.stdin.readline
N = int(input())
graph = {i : {'w' : 0, 'num' : 0, 'nodes' : []} for i in range(1,N+1)}
DP  = [0] * (N+1)
stack = collections.deque()
for i in range(1,N+1) :
  S = list(map(int,input().split()))
  graph[i]['w'] = S[0]
  DP[i] = S[0]
  graph[i]['num'] = S[1]
  if graph[i]['num'] == 0:
    stack.append(i)
  for j in range(S[1]) :
    graph[S[2+j]]['nodes'].append(i)
ans = 0
while stack :
  tmp= stack.popleft()
  for node in graph[tmp]['nodes'] :
    graph[node]['num'] -= 1
    DP[node] = max(DP[node], DP[tmp] + graph[node]['w'])
    if graph[node]['num'] == 0 :
      stack.append(node)
print(max(DP))

