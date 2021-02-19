import sys 
sys.stdin = open("./Algorithm_Study/0219/lab01", "r")
N = int(input())
arr = list(map(int, input().split()))
K = int(input())
leaf = [1] *N 
for i in range(N) :
  if arr[i] == -1 :
    leaf[i] == 0
    continue
  if i == K :
    leaf[i] = 0
    continue
  if arr[i] == K : 
  else :
    leaf[arr[i]] = 0

print(leaf)

