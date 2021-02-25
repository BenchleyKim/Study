import sys 
import heapq
sys.stdin = open("./Algorithm_Study/BOJ/BOJ7662", "r")

T = int(sys.stdin.readline())
for _ in range(T) :
  MXQ = []
  MNQ = []
  K = int(sys.stdin.readline())
  length = 0
  for _ in range(K) :
    C, N = sys.stdin.readline().split()
    N = int(N)
    if C == 'I' :
      heapq.heappush(MNQ,N)
      heapq.heappush(MXQ,-N)
      length += 1
      continue
    if C == 'D' :
      if length == 0 :
        MXQ = []
        MNQ = []
        continue
      length -= 1
      if N == 1 :
        # 최대값 삭제
        mx = heapq.heappop(MXQ)
        continue
      if N == -1 :
        # 최소값 삭제
        mn = heapq.heappop(MNQ)
        continue
  if length == 0 :
    print('EMPTY')
  else :
    # 최대값 , 최소값 출력 
    print(-(heapq.heappop(MXQ)),heapq.heappop(MNQ))
    
