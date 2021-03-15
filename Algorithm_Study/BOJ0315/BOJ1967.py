import sys

sys.stdin = open("./Algorithm_Study/BOJ0315/BOJ1967", "r")

N = int(sys.stdin.readline())
if N == 1 :
  print(-1)
else :
  tree = {}
  nodeSet = {1:0}
  mx = 0
  start = 1
  for _ in range(N-1) :
    P, C, W = map(int, sys.stdin.readline().split())
    if P in tree.keys():
      tree[P][C] = W
    else :
      tree[P] = {C:W}
    if C in tree.keys():
      tree[C][P] = W
    else :
      tree[C] = {P:W}
    nodeSet[C] = nodeSet[P] + W
    if nodeSet[C] > mx : 
      mx = nodeSet[C]
      start = C
  check = {}
  for n in nodeSet.keys() :
    check[n] = -1
  stack = [[start,0]]
  mx = 0
  while stack :
    tmp,w = stack.pop()
    if check[tmp] != -1:
      continue
    check[tmp] = w
    if mx < check[tmp] :
      mx = check[tmp]
    subs = tree[tmp].keys()
    for s in subs :
      if  check[s] != -1:
        continue
      stack.append([s,tree[tmp][s] + check[tmp]])
  print(mx)

