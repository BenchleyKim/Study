import sys
import queue
import heapq
sys.stdin = open('./Algorithm_study/0218/lab02','r')
INF = 10001
N, K = map(int, input().split())
queue = []
arr = list(map(int, input().split()))
sum = 0 
for i in range(N) :
  heapq.heappush(queue, arr[i])
  print(queue)
  if i >= K-1 : 
    heapq.heapify(queue)
    # print(i,arr[i-K+1])
    print(arr[i-(K//2)])
    sum += arr[i-(K//2)]
    queue.remove(arr[i-K+1])
    
    
print(sum)