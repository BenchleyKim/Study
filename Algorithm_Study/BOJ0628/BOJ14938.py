import sys
sys.stdin = open("./Algorithm_Study/BOJ0628/BOJ14938","r")
input = sys.stdin.readline

N , M , R = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = {}
for i in range(R) :
    a , b, l =  map(int, input().split())
    if a in graph :
        graph[a][b] = l
    else :
        graph[a] = {b : l}
    if b in graph :
        graph[b][a] = l
    else :
        graph[b] = {a : l}
mx_itmes = 0
for node in graph.keys() :
    queue = []
    for sub in graph[node].keys() :
        if graph[node][sub] <= M :
            queue.append((sub,graph[node][sub] ))
    local_check = [0] * (N+1)
    total_items = items[node]
    while queue :
        n, cnt = queue.pop()
        if local_check[n] :
            continue
        local_check[n] = 1
        total_items += items[n]
        for sub in graph[n].keys() :
            if graph[n][sub] + cnt <= M :
                queue.append(sub, graph[n][sub] + cnt )
    mx_itmes = max(total_items, mx_itmes)
print(items)
print(mx_itmes)


