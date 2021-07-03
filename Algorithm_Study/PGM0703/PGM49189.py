import heapq
import sys
def solution(n, edge):
    answer = 0
    heap = []
    graph = {}
    for s, e in edge : 
        if s in graph  :
            graph[s].append(e)
        else :
            graph[s]  = [e]
        if e in graph :
            graph[e].append(s)
        else :
            graph[e]  = [s]
    heapq.heappush(heap, (0,1))
    INF = sys.maxsize
    check = [INF] * (n+1)
    while heap :
        distance, node = heapq.heappop(heap)
        if check[node] <= distance :
            continue
        check[node] = distance
        for sub in graph[node] :
            heapq.heappush(heap, ( distance + 1, sub))
    check[0] = 0
    mx = max(check)
    answer = check.count(mx)
                
        
        
        
    return answer