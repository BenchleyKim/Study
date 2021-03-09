import sys
sys.stdin = open('./Algorithm_study/0217/lab04','r')
n = int(input())
arr = [0]+list(map(int, input().split()))


DP = [0]
def lowerBound(start,end,target) :
  while end > start :
    mid = (start+end)//2
    if DP[mid] >= target :
      end = mid 
    else:  
      start = mid+1
  return end

for a in arr :
  if DP[-1] < a :
    DP.append(a)
  elif DP[-1] > a:
    i = lowerBound(0,len(DP),a)
    DP[i] = a
  print(DP)

print(n-(len(DP)-1))
    

DP = [0]*(n+1)
 
for i in range(1,n+1):
    for j in range(1, i, 1):
        if arr[i] > arr[i-j]:
            DP[i] = max(DP[i-j], DP[i])
    DP[i] += 1
    print(DP)
print(n - max(DP))