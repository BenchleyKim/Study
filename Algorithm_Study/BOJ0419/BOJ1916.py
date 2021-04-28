import sys
import heapq
sys.stdin = open("./Algorithm_Study/BOJ0419/BOJ1916","r")
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = {i : {} for i in range(1,N+1)}
for i in range(M) :
    a, b, c = map(int, input().split())
    if graph[a].get(b) :
        if graph[a][b] <= c:
            continue
        else :
            graph[a][b] = c
    else :
        graph[a][b] = c
s, e = map(int, input().split())

INF = sys.maxsize
check = [INF] * (N+1)

stack = []
heapq.heappush(stack, (0,s))
while stack :
    dist, node = heapq.heappop(stack)
    if check[node] <= dist :
        continue
    check[node] = dist 
    for sub in graph[node].keys() :
        if check[sub] <= dist + graph[node][sub] :
            continue
        heapq.heappush(stack,(dist+graph[node][sub], sub))

print(check[e])

