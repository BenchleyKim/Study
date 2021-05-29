import sys
from collections import deque
import heapq 
sys.stdin = open(".\Algorithm_Study\BOJ0529\BOJ21773","r")
input = sys.stdin.readline

T, n = map(int, input().split())
heap = []

for i in range(n) :
    a, b, c = map(int, input().split())
    heapq.heappush(heap, (-c,a,b))
for t in range(T) :
    c, a, b = heapq.heappop(heap)
    print(a)
    b -= 1
    if b <= 0 :
        continue
    else :
        heapq.heappush(heap, (c+1,a,b))
