import sys
import collections
sys.stdin = open("./Algorithm_Study/BOJ0325/BOJ11437", "r")
input = sys.stdin.readline
N = int(input())
INF = sys.maxsize

tree = {}
for i in range(N-1) :
  A, B = map(int,input().split())
  if A in tree.keys():
    tree[A].append(B)
  else :
    tree[A] = [B]
  if B in tree.keys() :
    tree[B].append(A)
  else :
    tree[B] = [A]
queue = [[1,1]] 
check = [0] * (N+1)
parent_tree = {}
parent_tree[1] = -1
check[1] = 1
while queue :
  node , r= queue.pop(0)   
  for sub in tree[node] :
    if check[sub] :
      parent_tree[node] = sub
      continue
    check[sub] = r+1
    queue.append([sub,r+1])
M = int(input())
for _ in range(M) :
  A,B = map(int, input().split())
  q1 ,q2 = A, B
  # q1 이 상위랭크(작음) q2 는 하위랭크(큼)
  if check[A] > check[B] :
    q1 ,q2 = B, A
  q1rank, q2rank = check[q1], check[q2]
  while check[q1] != check[q2] :
    q2 = parent_tree[q2]
  if q1 == q2 :
    print(q1)
    continue
  else :
    while q1 != q2 :
      q1 = parent_tree[q1]
      q2 = parent_tree[q2]
    print(q1)

    
