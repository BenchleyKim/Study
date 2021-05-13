from collections import deque

def solution(values, edges, queries):
    answer = []
    graph = {}
    for edge in edges :
        v1, v2 = edge
        if graph.get(v1) :
            graph[v1].append(v2)
        else :
            graph[v1] = [v2]
        if graph.get(v2) :
            graph[v2].append(v1)
        else :
            graph[v2] = [v1]
    print(graph)
    queue = deque([(1,0)])
    ranks = [0] * (len(values)+1)
    check = [0] * (len(values)+1)
    while queue :
        node,rank = queue.popleft()
        if check[node] :
            continue
        ranks[node] = rank
        check[node] = 1 
        for sub in graph[node] :
            queue.append((sub, rank+1))
    print(ranks)
    for qur in queries :
        u, w = qur 
        if w == -1 :
            ans = 0
            queue = deque([u]) 
            check = [0] * (len(values)+1)
            while queue :
                node = queue.pop()
                if check[node] :
                    continue
                check[node] = 1 
                ans += values[node-1]
                for sub in graph[node] :
                    if ranks[sub] > ranks[node] :
                        queue.append(sub)
            answer.append(ans)
        else : 
            values[u-1] = 0
            while True :
                parent = 0 
                for sub in graph[u] :
                    if ranks[sub] < ranks[u] :
                        parent = sub
                        break
                if parent == 0 :
                    values[u-1] = w 
                    break
                values[u-1] = values[parent-1]
                u = parent


    return answer



print(solution([1,10,100,1000,10000],	[[1,2],[1,3],[2,4],[2,5]],	[[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[4,1000],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[2,1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1]]))
