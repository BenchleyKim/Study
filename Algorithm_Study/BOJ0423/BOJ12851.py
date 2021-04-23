import sys
import heapq 
sys.stdin = open("./Algorithm_Study/BOJ0423/BOJ12851","r")
input = sys.stdin.readline

N, K = map(int, input().split())

heap = []
heapq.heappush(heap,(0,N))
mndist = sys.maxsize
check = [0] * 1000001
while heap :
    dist, node = heapq.heappop(heap)
    if node >= len(check) or node <= 0 :
        continue
    if check[node] :
        continue
    check[node] = 1
    if node == K :
        print(dist)
        mndist = dist
        break
    if node < K : 
        if node+1 < 1000001 :
            heapq.heappush(heap, (dist+1, node+1))
        if node*2 < 1000001 :
            heapq.heappush(heap,(dist+1, 2*node))
    heapq.heappush(heap,(dist+1, node-1))
cnt = 1
while heap :
    if heap[0][0] != mndist :
        break
    if heap[0][1] == K :
        cnt += 1
    dist, node = heapq.heappop(heap)
print(cnt)