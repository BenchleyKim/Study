import sys

def solution(n, z, roads, queries):
    answer = []
    # INF = sys.maxsize
    INF = 100
    graph = {i : {} for i in range(n) }
    DP = [[INF] * 2 for _ in range(51)]
    for road in roads :
        u,v,w = road 
        graph[u][v] = w
        DP[w][0] = 1
        DP[w][1] = v
        for i in range(w,len(DP)-w) :
            if DP[i+w][0] > DP[i][0]+DP[w][0]+ 1:
                DP[i+w][0] = DP[i][0] + DP[w][0]+ 1
                DP[i+w][1] = v
    DP[z][0] = 1
    DP[z][1] = 0
    for i in range(z,len(DP)-z) :
        if DP[i+z][0] > DP[i][0] + DP[z][0] : 
            DP[i+z][0] = DP[i][0] + DP[z][0]
            DP[i+z][1] = DP[i][1]
    # for idx, d in enumerate(DP) :
    #     print(idx, d)
    stack = [0]
    check = [0] * n
    while stack :
        node = stack.pop()
        if check[node] :
            continue
        check[node] = 1
        stack.extend(graph[node].keys())
    # print(check)

    for q in queries :
        mn = INF
        if q == 0 :
            mn = 0 
            answer.append(mn)         
            continue     
        for i in range(1,len(DP)) :
            div, mod = divmod(q,i)

            if DP[mod][0] == INF :
                continue
            if check[DP[mod][1]] :
                mn = min(mn, div * (DP[i][0] +1)+ DP[mod][0])
            else :
                mn = min(mn, div * (DP[i][0]+1) + DP[mod][0] + 1)
        if mn >= INF :
            answer.append(-1)
        else :
            answer.append(mn)
                
            



    return answer

    

print(solution(5,5,[[1,2,3],[0,3,2]],[0,1,2,3,4,5,6]))