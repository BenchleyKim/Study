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

t = 0 
while True :
    if t > T :
        break
    t += 1
    if heap :
        c, a, b = heapq.heappop(heap)
        gap = heap[0][0] - c
        for g in range(gap) :
            print(a) 
            t += 1
            b -= 1
            if b <= 0 :
                break
        if b <= 0 :
            continue
        else :
            heapq.heappush(heap,(c+gap,a,b))
    else :
        break