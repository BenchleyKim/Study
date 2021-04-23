import sys
import heapq
from collections import deque
sys.stdin = open("./Algorithm_Study/BOJ0423/BOJ16953","r")
input = sys.stdin.readline

A, B = map(int, input().split())
queue = deque([(0,A)])
queue = []
heapq.heappush(queue, (0,B))
endFlag = False
while queue :
    dist, node  = heapq.heappop(queue)
    if node == A :
        print(dist+1)
        endFlag = True
        break
    if node == 0 :
        continue
    if node % 2 == 0 :
        heapq.heappush(queue,(dist+1, node//2))
    if node % 10 == 1 :
        heapq.heappush(queue, (dist+1,(node-1)//10))
if not endFlag :
    print(-1)