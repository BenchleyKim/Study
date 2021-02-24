import sys
sys.stdin = open("./Algorithm_Study/BOJ/BOJ11723", "r")

M = int(sys.stdin.readline())
empty = [0] * 21
all = [1] * 21
tmp =[0] * 21
for _ in range(M) :
  S = sys.stdin.readline().strip()
  if S == 'all' :
    tmp = all
    continue
  if S == 'empty' :
    tmp = empty
    continue
  S, x = S.split()
  x = int(x)
  if S == 'add' :
    tmp[x] = 1
    continue
  if S == 'remove' :
    tmp[x] = 0
    continue
  if S == 'check' :
    if tmp[x] == 1:
      print(1)
      continue
    print(0)
    continue
  if S == 'toggle' :
    if tmp[x] == 1:
      tmp[x] = 0
    else :
      tmp[x] = 1
    continue
  
  