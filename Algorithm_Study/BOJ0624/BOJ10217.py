import sys
sys.stdin = open(".\Algorithm_Study\BOJ0624\BOJ10217","r")
input = sys.stdin.readline

T = int(input())
for t in range(T) :
    N , M , K = map(int, input().split())
    graph = {}
    cost_check  = [0] * (N+1)
    dist_check = [0] * (N+1)
    for k in range(K) :
        u, v, c , d = map(int, input().split())
        if graph.get(u) :
            graph[u][v] = [c,d]
        else :
            graph[u] = {v:[c,d]}
    print(graph)

