from os import rename
import sys
sys.stdin = open(".\Algorithm_Study\BOJ0513\BOJ14657","r")
input = sys.stdin.readline

N, T = map(int, input().split())
graph = {}
for i in range(N-1) :
    A, B, W = map(int, input().split())
    if graph.get(A) :
        graph[A][B] = W
    else :
        graph[A] = {B:W}
    if graph.get(B) :
        graph[B][A] = W
    else :
        graph[B] = {A:W}
stack = [(1,0)]
INF = sys.maxsize
check = [INF] * (N+1)
mxdist = 0
while stack :
    node, dist = stack.pop()
    if check[node] <= dist:
        continue
    check[node] = dist
    mxdist = max(dist,mxdist)
    for sub in graph[node].keys() :
        stack.append((sub,dist+1))
roots = []
for i in range(N+1) :
    if check[i] == mxdist :
        roots.append(i)
mn = INF
for root in roots :
    stack = [(root,0,0)]
    check = [INF] * (N+1)
    ranks = [INF] * (N+1)
    mxdist = 0
    while stack :
        node , rank , dist = stack.pop()
        if check[node] <= dist :
            continue
        check[node] = dist
        ranks[node] = rank
        mxdist = max(dist,mxdist)
        for sub in graph[node].keys() :
            stack.append((sub,ranks[node]+ graph[node][sub], dist+1))
    leafs =[]
    for i in range(N+1) :
        if check[i] == mxdist :
            leafs.append(i)
            mn = min(mn, ranks[i])
            
ans = mn // T 
if ans % T :
    ans += 1
print(ans)
    

