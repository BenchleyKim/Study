import sys
import math
sys.stdin = open('./Algorithm_study/0218/lab01','r')

S, P = map(int, input().split())
m = min(S,P)
e = math.exp(1)

localMax = int(P//e + 1)
print(localMax)
result = - 1 
def binSearch(start, end) :
  mid = (start+end) // 2 
  if start == end : 
    result = -1
    return 
  if float(S/mid) == float( P**(1/mid)) :
    result = mid
    return 
  if float(S/mid) <= float( P**(1/mid)) :
    binSearch(mid+1,end)
  else :
    binSearch(start, mid)

if P == S : result = 1
else : 
  binSearch(1, localMax)

print(result)