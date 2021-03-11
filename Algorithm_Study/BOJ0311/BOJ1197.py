import sys
import heapq
sys.stdin = open("./Algorithm_Study/BOJ0311/BOJ1197", "r")

heap = []

V , E = map(int , sys.stdin.readline().split())
for _ in range(E) :
  A, B ,C = map(int ,sys.stdin.readline().split())
  heapq.heappush(heap, (C,A,B))
check = [0] * (V+1)
weight = [0] * (V+1)
ans = 0
C, A ,B = heapq.heappop(heap)
ans = C 
check[A] = check[B] = A
print(A,B,check)

while heap :
  C, A, B = heapq.heappop(heap)
  if check[A] == check[B] and check[A] != 0 and check[B] != 0:
    continue
  ans += C
  print(A, B,check)
  if check[A] == 0 and check[B] == 0 :
    check[A] = check[B] = A
    continue
  if check[A] == 0 :
    check[A] = check[B]
    continue
  if check[B] == 0 :
    check[B] = check[A]
    continue
  check[A] = check[B]


print(ans)

