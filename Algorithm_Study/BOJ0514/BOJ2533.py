import sys
sys.stdin = open(".\Algorithm_Study\BOJ0514\BOJ2533","r")
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


N = int(input())
graph = {i:[] for i in range(1,N+1)}

for i in range(N-1) :
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
DP = [[0,0]] * (N+1)
check = [[0,0]] * (N+1)

stack = [(1,True)]
# flag 얼리 어답터인지 아닌지 
def dfs(node, flag) :
    if len(graph[node]) == 1 :
        if flag :
            DP[node][0] = 1
            
        else :
            DP[node][1] = 0 
        return DP[node][0]
    
    if flag :
        check[node][0] = 1
        for sub in graph[node] :
            if check[sub][1] :
                continue
            DP[node][0] += min(dfs(sub,True), dfs(sub,False))
        return DP[node][0]
    else :
        check[node][1] = 1
        for sub in graph[node] :
            if check[node][0]  :
                continue
            DP[node][1] += dfs(sub,True)
        return DP[node][1]

ans = min(dfs(1,True), dfs(1,False))

print(ans)




