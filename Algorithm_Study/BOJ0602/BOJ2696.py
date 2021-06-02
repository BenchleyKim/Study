import sys
import heapq
sys.stdin = open(".\Algorithm_Study\BOJ0602\BOJ2696","r")
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    M = int(input())
    arr = list(map(int, input().split()))
    minheap = []
    maxheap = []
    base = arr[0]
    heapq.heappush(maxheap, -base)
    for idx, a in enumerate(arr) :
        if (idx+1) % 2 :
            if len(minheap) > len(maxheap) :
                base = minheap[0]
            elif len(minheap) < len(maxheap) :
                base = -maxheap[0]
            print(base,end=" ")
        if a >= base :
            heapq.heappush(minheap,a)
        else :
            heapq.heappush(maxheap,-a)
    print(arr)