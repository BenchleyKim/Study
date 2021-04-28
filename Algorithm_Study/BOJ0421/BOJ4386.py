import sys
import heapq
sys.stdin = open("./Algorithm_Study/BOJ0421/BOJ4386","r")
input = sys.stdin.readline

N = int(input())
arr = []
graph = {i : {} for i in range(N) }
for i in range(N) :
    x,y = list(map(float, input().split()))
    for idx , a in enumerate(arr) : 
        dist = round(((a[0]-x)**2 + (a[1]-y)**2)**(1/2),2)
        graph[i][idx] = dist
        graph[idx][i] = dist
    arr.append([x,y])


heap = []
heapq.heappush(heap, (0,0))
check = [0] * N
ans = 0
while heap :
    dist, node =heapq.heappop(heap)
    if check[node] :
        continue
    check[node] = 1
    ans += dist
    for sub in graph[node].keys() :
        heapq.heappush(heap,(graph[node][sub],sub))
print(ans)
    
