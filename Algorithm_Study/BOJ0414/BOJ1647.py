import sys
import heapq
sys.stdin = open("./Algorithm_Study/BOJ0414/BOJ1647","r")
input = sys.stdin.readline


N, M = map(int, input().split())
graph = {i : {} for i in range(1,N+1) }
for i in range(M) :
    A, B, C = map(int, input().split())
    graph[A][B] = C
    graph[B][A] = C

heap = []
for sub in graph[1].keys():
    heapq.heappush(heap, (graph[1][sub], sub))

check = [0] *(N+1)
total_cost = 0
mx = 0
check[1] = 1
while heap :
    cost, node = heapq.heappop(heap)
    if check[node] :
        continue
    check[node] = 1
    total_cost += cost
    mx = max(mx, cost)
    for sub in graph[node].keys() :
        heapq.heappush(heap,(graph[node][sub],sub))
print(total_cost-mx)
    

