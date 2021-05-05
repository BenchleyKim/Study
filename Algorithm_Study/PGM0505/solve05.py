



def solution(n, path, orders):
    graph = {i : {'p' : i,'sub' : []} for i in range(N)}
    rank = [1024] * n 
    rank[0] = 0
    for p in path :
        a, b = p
        if rank[a] < rank[b] :
            graph[a]['sub'].append(b)
            graph[b]['p'] = a
        else :
            graph[b]['sub'].append(a)
            graph[a]['p'] = b
            

    print(graph)
    check = [0] * n 
    order = [-1] * n
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
        if order[node] != -1:
            stack.append(order[node])
            check[order[node]] = 0
        if graph.get(node) :
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