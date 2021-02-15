import sys 
sys.stdin = open("./Algorithm_Study/0215/lab03", "r")

N = int(input())
K = int(input())
D = {}
for _ in range(K) :
  x ,y  = map(int, input().split())
  if x not in D.keys() :
    D[x] = {y}
  if y not in D.keys():
    D[y] = {x}
  D[y].add(x)
  D[x].add(y)
print(D)
  


R = int(input())
for _ in range(R) :
  s ,e = map(int, input().split())
  stack = [s]
  cstack =[0]
  check = [0] * (N+1)
  count = 0
  while len(stack) != 0 : 
    node = stack.pop()
    count = cstack.pop()
    # print(node)
    if node == e :
      check[e] = 1
      print( count)
      break
    if check[node] == 1:
      continue
    count += 1
    check[node] = 1
    l = D[node]
    for n in l :
      stack.append(n)
      cstack.append(count)
  # print(check)
  if check[e] == 0 :
    print(-1)
    continue
  
  # print("check : ",check)

