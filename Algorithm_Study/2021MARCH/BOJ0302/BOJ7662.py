import sys 
import heapq
sys.stdin = open("./Algorithm_Study/BOJ0302/BOJ7662", "r")

T = int(sys.stdin.readline())

for _ in range(T) :
  K = int(sys.stdin.readline())
  arr = []
  mxheap  = []
  mnheap = []
  check = [0] * 1000001
  for i in range(K) :
    Q, N =  sys.stdin.readline().split()
    N = int(N) 
    if Q == 'I' :
      arr.append(N)
      heapq.heappush(mxheap, (-1 * N, i))
      heapq.heappush(mnheap, (N, i))
      check[i] = 1
      
    elif Q == 'D' :
      if len(arr) == 0 :
        continue
      if N == 1 :
        # 최대값 삭제
        while mxheap and not check[mxheap[0][1]] :
          heapq.heappop(mxheap)  
        if mxheap :
          check[mxheap[0][1]] = False
          heapq.heappop(mxheap)
        continue
      if N == -1 :
        # 최소값 삭제
        while mnheap and not check[mnheap[0][1]] :
          heapq.heappop(mnheap)
        if mnheap :
          check[mnheap[0][1]] = False
          heapq.heappop(mnheap)  
        continue
  while mnheap and not check[mnheap[0][1]] : heapq.heappop(mnheap)
  while mxheap and not check[mxheap[0][1]] : heapq.heappop(mxheap)
  if mxheap and mnheap :
    print(-1*(mxheap[0][0]), mnheap[0][0])
  else :
    print("EMPTY")

