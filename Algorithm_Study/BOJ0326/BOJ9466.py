import sys
import collections
sys.stdin = open("./Algorithm_Study/BOJ0326/BOJ9466", "r")
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
  N = int(input())
  arr = list(map(int, input().split()))
  tree = {}
  for i in range(N) :
    tree[i+1] = arr[i]
  check = [0] * (N+1)
  cnt = N
  for i in range(N) :
    if check[i+1] :
      cnt -= 1
      continue
    stack = collections.deque([tree[i+1]])
    team = [i+1]
    flag = False
    while stack :
      node = stack.pop()
      if node == i+1 :
        flag = True
        break
      if check[node] :
        continue
      team.append(node)
      check[node] = 1
      stack.append(tree[node])
    if flag :
      cnt -= 1
      for member in team :
        check[member] = 1
    else :
      for member in team :
        check[member] = 0
  print(cnt)