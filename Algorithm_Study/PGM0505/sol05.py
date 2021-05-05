



def solution(n, path, orders):
    graph = {}
    for p in path :
        a, b = p
        if graph.get(a) :
            graph[a][b] = 1
        else :
            graph[a] = {b:1}
        if graph.get(b) :
            graph[b][a] = 1
        else :
            graph[b] = {a:1} 
    # print(graph)
    check = [0] * n 
    order = [0] * n
    for o in orders :
        a, b = o
        order[a] = b
        check[b] = -1
        
    stack = [0]
    while stack :
        node = stack.pop()
        if check[node] :
            continue
        check[node] = 1
        if order[node] :
            locked = order[node] 
            for sub in graph[locked].keys() :
                if check[sub] == 1 :
                    stack.append(order[node])
                    break
            check[order[node]] = 0
        for sub in graph[node].keys() :
            if check[sub] :
                continue
            stack.append(sub)
    answer = True
    # print(check)
    for i in range(n) :
        if check[i] == -1 or check[i] == 0:
            answer = False
            break
    
    return answer



print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[8,5],[6,7],[4,1]]))
print(solution(9,[[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]],[[4,1],[5,2]]))
print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[4,1],[8,7],[6,5]]))