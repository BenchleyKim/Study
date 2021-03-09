import sys 
sys.stdin = open("./Algorithm_Study/0215/lab01", "r")
t = int(input())
def lis(arr):
    if not arr:
        return 0
    
    ret = 1
    for i in range(len(arr)):
        nxt = []
        for j in range(i+1, len(arr)):
            if arr[i] <= arr[j]:
                nxt.append(arr[j])
        ret = max(ret, 1 + lis(nxt))
    return ret	

for _ in range(t) :
  n = int(input())
  l = list(map(int,input().split()))
  print("lis : ", lis(l), l)
  countSum = 0
  check = [0] * n
  for i in range(n) :
    check[i] = 1
    for j in range(i,n):
      if l[i] > l[j] :
        check[i] = max(check[i], check[j]+1)
  # print(check)
  # print(len(l)-max(check))
  
