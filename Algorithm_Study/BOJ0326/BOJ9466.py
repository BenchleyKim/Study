import sys
sys.stdin = open("./Algorithm_Study/BOJ0326/BOJ9466", "r")
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
  N = int(input())
  tree = [0] + list(map(int, input().split()))
  check = [0] * (N+1)
  cnt = N
  group = 1
  for i in range(1,N+1) :
    if check[i] :
      continue
    while check[i] == 0 :
      check[i] = group
      i = tree[i]
    while check[i] == group :
      check[i] = -1
      i = tree[i]
      cnt -= 1
    group += 1
  print(cnt)