import sys 
sys.stdin = open("./Algorithm_Study/BOJ0305/BOJ11725", "r")

N = int(sys.stdin.readline())
check = [0] * (N+1)
tree = {i:[] for i in range(1,N+1)}
while True :
  INPUT =  sys.stdin.readline()
  if INPUT == '' :
    break
  s, e = map(int,INPUT.split())
  tree[s].append(e)
  tree[e].append(s)

parents = [0] * (N+1)
queue = [1]
while queue :
  tmp = queue.pop(0)
  if check[tmp] :
    continue
  check[tmp] = 1
  for i in tree[tmp] :
    queue.append(i)
    if parents[i] :
      continue
    parents[i] = tmp
    
for i in range(2,len(parents)):
  print(parents[i])