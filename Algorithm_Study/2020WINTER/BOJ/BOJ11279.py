import sys 
sys.stdin = open("./Algorithm_Study/BOJ/BOJ1279", "r")

heap = [0]

N = int(sys.stdin.readline())
for _ in range(N) :
  X = int(sys.stdin.readline())
  l = len(heap)
  # print(X, heap)
  if X == 0 :
    if l == 1 :
      print(0)
      continue
    print(heap[1])
    heap[1], heap[l-1] = heap[l-1], heap[1]
    heap.pop()
    n =1 
    while 2*n <= l-2 :
      tmp = 2*n
      if 2*n+1 < l-2 :
        if heap[2*n+1] > heap[2*n] :
          tmp = 2*n+1
      # print("n : " ,n, tmp,heap)
      if heap[n] < heap[tmp] : 
        heap[n], heap[tmp] = heap[tmp] , heap[n]
        n = tmp
      else :
        break
    continue
  heap.append(X)
  while X > heap[l//2] and l != 1 :
    heap[l//2], heap[l] = heap[l], heap[l//2]
    l //= 2
