import sys
import heapq
sys.stdin = open(".\Algorithm_Study\SFR0626\SFR395","r")
input = sys.stdin.readline

W, N = map(int, input().split())
heap = []
for i in range(N) :
    m, p = map(int, input().split())
    heapq.heappush(heap, (-p, m))
answer = 0 
cnt = 0 
while heap :
    p, m = heapq.heappop(heap) 
    p = -p
    if cnt + m > W :
        answer += (W-cnt) * p
        break
    answer += m * p
    cnt += m
print(answer)