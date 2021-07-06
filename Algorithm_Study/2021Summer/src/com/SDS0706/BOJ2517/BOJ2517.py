import sys
import heapq
sys.stdin = open("./Algorithm_Study/2021Summer/src/com/SDS0706/BOJ2517/BOJ2517.in","r")
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N) :
    data = int(input())
    heapq.heappush(heap, (-data, i))
cnt = 0
while heap :
    data , idx = heapq.heappop(heap)
    print(cnt ,data, idx)
    cnt += 1

