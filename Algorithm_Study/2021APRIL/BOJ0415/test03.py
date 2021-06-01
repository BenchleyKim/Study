from collections import deque

def solution(a, edges):
    answer = 0
    graph = {i : [] for i in range(len(a))}
    sublist = [0]*len(a)
    for e in edges :
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        sublist[e[0]] += 1
        sublist[e[1]] += 1
    queue = deque()
    for p in graph.keys():
        if len(graph[p]) == 1 :
            queue.append(p)
    check = [0]*len(a)

    while queue :
        node = queue.popleft()
        if check[node]  :
            
            continue
        if sublist[node] == 0 :
            if a[node] != 0 :
                answer = -1
            break
        k = a[node]
        a[node] = 0
        check[node] = 1
        sublist[node] -= 1
        answer += abs(k)
        for sub in graph[node] :
            if check[sub] :
                continue
            sublist[sub] -= 1
            a[sub] += k
            if sublist[sub] == 1 :
                queue.append(sub)

    
    return answer

print(solution([0,1,0],	[[0,1],[1,2]]))
print(solution([-5,0,2,1,2],	[[0,1],[3,4],[2,3],[0,3]]))