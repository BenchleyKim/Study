import sys
import heapq
sys.stdin = open("./Algorithm_Study/BOJ/BOJ1927", "r")
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
  x = int(sys.stdin.readline())
  if x == 0 :
    if not heap :
      print(0)
      continue
    print(heapq.heappop(heap))
  else : 
    heapq.heappush(heap, x)