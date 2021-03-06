import sys 
from collections import deque
import heapq
sys.stdin = open("./Algorithm_Study/BOJ0306/BOJ13549", "r")
MAX = 100000
N, K = map(int, sys.stdin.readline().split())

queue = [(0,N)]

check = [0] * MAX * 2
while queue :
  count, tmp = heapq.heappop(queue)
  if tmp == K : 
    print(count)
    break
  if tmp >= 2*MAX or tmp < 0 : 
    continue
  if check[tmp] == 1 :
    continue
  check[tmp] = 1
  heapq.heappush(queue, (count,2*tmp))
  heapq.heappush(queue, (count+1,tmp-1))
  heapq.heappush(queue, (count+1,tmp+1))

