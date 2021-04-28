import sys 
import heapq
sys.stdin = open("./Algorithm_Study/BOJ0301/BOJ11279", "r")

N = int(sys.stdin.readline())
heap = []
for _ in range(N) :
  k = int(sys.stdin.readline())
  if k == 0 :
    if heap :
      print(-(heapq.heappop(heap)))
    else :
      print(0)
  else : 
    heapq.heappush(heap,-k)



