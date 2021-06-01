import sys
import heapq
from collections import deque
sys.stdin = open("./Algorithm_Study/BOJ0415/BOJ1238","r")
input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = {i : {} for i in range(1,N+1)}

for i in range(M) :
    A, B, T  = map(int,input().split())
    graph[A][B] = T

mx = 0
stack = []
heapq.heappush(stack,(0,X))
INF = sys.maxsize
xDP = [INF]* (N+1)
while stack :
    distance, node  = heapq.heappop(stack)
    if xDP[node] > distance :
        xDP[node] = distance
        for sub in graph[node].keys() :
            heapq.heappush(stack,(distance+graph[node][sub], sub) )
    else :
        continue
for i in range(1,N+1) :
    stack = []
    heapq.heappush(stack,(0,i))
    INF = sys.maxsize
    DP = [INF]* (N+1)
    while stack :
        distance, node  = heapq.heappop(stack)
        if DP[node] > distance :
            DP[node] = distance
            for sub in graph[node].keys() :
                heapq.heappush(stack,(distance+graph[node][sub], sub) )
        else :
            continue
    mx = max(mx, DP[X]+xDP[i])
    
print(mx)