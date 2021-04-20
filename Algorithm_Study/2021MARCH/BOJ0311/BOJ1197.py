import sys
import heapq
sys.stdin = open("./Algorithm_Study/BOJ0311/BOJ1197", "r")

heap = []

V , E = map(int , sys.stdin.readline().split())
for _ in range(E) :
  A, B ,C = map(int ,sys.stdin.readline().split())
  heapq.heappush(heap, (C,A,B))
check = [v for v in range(V+1)]
ans = 0

def find_root(node) :
  tmp = node
  while check[node] != node :
    node = check[node]
  check[tmp] = node
  return node

while heap :
  C, A, B = heapq.heappop(heap)
  if find_root(A) == find_root(B) :
    continue
  check[find_root(A)] = find_root(B)
  ans += C

print(ans)

