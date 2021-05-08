def solution(n, start, end, roads, traps):
    answer = 0
    graph = {i:{} for i in range(1,n+1)}
    for road in roads :
        p, q, s =road 
        graph[p][q] = s
        graph[q][p] = -s
    print(graph)
    stack = [(start,0)]
    while stack :
        node, time = stack.pop()
        if node == end :
            answer = time
            break
        if node in traps :
            for sub in graph[node].keys() :
                graph[sub][node] = -graph[sub][node]
                graph[node][sub] = -graph[node][sub]

        for sub in graph[node].keys() :
            if graph[node][sub] > 0 :
                stack.append((sub, time+graph[node][sub]))

    return answer


print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2]))
print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2, 3]))