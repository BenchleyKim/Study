import sys 
sys.stdin = open("./Algorithm_Study/0219/lab01", "r")
N = int(input())
arr = list(map(int, input().split()))
K = int(input())

delList = [K]
newarr = []
if K == 0 :
  print(0)
  exit()
for i in range(N) :
  if arr[i] in delList :
    delList.append(i)
  else :
    if i == K :
      continue
    newarr.append(arr[i])
parentnode =[]
for i in newarr :
  if i in parentnode :
    continue
  else :
    parentnode.append(i)
print( len(newarr) - len(parentnode) + 1)

