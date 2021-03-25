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
rank = {}
while queue :
  node , r= queue.pop(0)
  if check[node] :
    continue
  check[node] = r
  if r in rank.keys() :
    rank[r].append(node)
  else :
    rank[r] = [node]    
  for sub in tree[node] :
    queue.append([sub,r+1])
M = int(input())
for _ in range(M) :
  A,B = map(int, input().split())
  q1 ,q2 = A, B
  # q1 이 상위랭크(작음) q2 는 하위랭크(큼)
  if check[A] > check[B] :
    q1 ,q2 = B, A
  queue = [[q1,check[q1]] ]
  flag = False
  while queue :
    tmp , r= queue.pop(0)
    if check[tmp] < r :
      continue
    if tmp == q2 :
      flag = True
      break
    for sub in tree[tmp] :
      queue.append([sub,r+1])
  if flag :
    print(q1)
  else :
    
    for i in range(check[q1]-1,0,-1) :
      control_flag= False
      for rank_root in rank[i] :
        queue = [[rank_root,check[rank_root]]]
        flag1 = False
        flag2 = False
        while queue :
          tmp , r= queue.pop(0)
          if check[tmp] < r :
            continue
          if tmp == q1 :
            flag1 = True
          if tmp == q2 :
            flag2 = True
          if flag1 & flag2 :
            break
          for sub in tree[tmp] :
            queue.append([sub,r+1])
        if flag2 & flag1 :
          print(rank_root)
          control_flag = True
          break
      if control_flag :
        break
