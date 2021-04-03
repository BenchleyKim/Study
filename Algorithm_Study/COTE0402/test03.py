import sys 
INF = sys.maxsize

def floyd_warshall(n,fares) : 
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, n + 1):
        graph[a][a] = 0
    # 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
    for fare in fares :
      c, d, f =fare
      graph[c][d] = f
      graph[d][c] = f

    # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(a+1, n + 1):
                graph[a][b] = graph[b][a] =  min(graph[a][b], graph[a][k] + graph[k][b])

    return graph
def solution(n, s, a, b, fares):
    distance = floyd_warshall(n,fares)
    mn = INF
    for i in range(1,n+1) :
        dist = distance[i][a] + distance[i][b] + distance[i][s]
        mn = min(mn,dist)
      
    answer = mn
    return answer

print(solution(6,4,6,2,	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))