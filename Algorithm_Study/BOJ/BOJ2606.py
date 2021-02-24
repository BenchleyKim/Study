import sys
sys.stdin = open("./Algorithm_Study/BOJ/BOJ2606", "r")

N = int(sys.stdin.readline())
V = int(sys.stdin.readline())
arr = {}
checkList = [0] * (N+1)

for _ in range(V) :
  a, b=  map(int,sys.stdin.readline().split())
  if a in arr.keys() :
    arr[a].append(b) 
  else : 
    arr[a] = [b]
  if b in arr.keys() :
    arr[b].append(a)
  else :
    arr[b] = [a]
  

s = 1 
stack = [s]
count = 0
while stack :
  tmp = stack.pop()
  if checkList[tmp] == 1 :
    continue
  checkList[tmp] = 1
  count += 1
  stack.extend(arr[tmp])

print(count-1)

