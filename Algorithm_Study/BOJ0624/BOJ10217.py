import sys
import heapq
sys.stdin = open(".\Algorithm_Study\BOJ0624\BOJ10217","r")
input = sys.stdin.readline

T = int(input())
INF = sys.maxsize
for t in range(T) :
    N , M , K = map(int, input().split())
    graph = {}
    DP = [[INF] * (M+1) for i in range(N+1)]
    for k in range(K) :
        u, v, c , d = map(int, input().split())
        if graph.get(u) :
            graph[u][v] = [c,d]
        else :
            graph[u] = {v:[c,d]}
    heap = []
    # 거리, 비용, 공항 번호
    heapq.heappush(heap, (0,0,1))
    answer = -1
    while heap :
        dist, cost, num  = heapq.heappop(heap)
        if cost > M :
            continue
        if num  == N  : 
            answer = dist
            break
        if dist < DP[num][cost]  :
            DP[num][cost] = dist 
            for sub in graph[num].keys() :
                heapq.heappush(heap,(dist + graph[num][sub][1], cost + graph[num][sub][0], sub)) 

    if answer < 0 :
        print("Poor KCM")
    else :
        print(answer)
    ## ruqclsms 

